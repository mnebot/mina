# Versionat i publicació

La distribució de PyPI es diu `mina-voice-assistant`; el nom d'import Python continua sent `mina`.

## Preparar el cicle de versió

1. A la primera PR del pròxim cicle de publicació, actualitza `project.version` a `pyproject.toml` amb la versió estable que es vol publicar, per exemple `0.1.1`.
2. No incrementis aquesta versió base per cada merge. Mantingues-la fins que la versió estable s'aprovi i es publiqui.
3. La CI valida cada PR. Després d'un merge validat a `master`, la pipeline deriva un prerelease únic com `0.1.1.dev42`, on `42` representa el run de GitHub Actions, i el publica a PyPI per provar-lo a les Raspberry Pi.

## Reintents i prereleases

- Un reintent del mateix run torna a generar el mateix número de versió.
- Si la mateixa versió i el mateix wheel ja existeixen a PyPI, es pot reutilitzar l'artefacte verificat pel seu SHA-256; no es torna a pujar.
- Si la versió existeix amb contingut diferent, la pipeline falla. Les versions de PyPI no es poden sobreescriure.
- Un prerelease concret es pot instal·lar així:

  ```sh
  python -m pip install --pre mina-voice-assistant==0.1.1.dev42
  ```

La pipeline de desplegament instal·la exactament el prerelease creat pel merge, no `latest`.

## Configurar la publicació de prereleases

Abans del primer merge que hagi de publicar un candidat:

1. Confirma que `mina-voice-assistant` està sota el control del propietari correcte a PyPI. El nom de projecte de PyPI no queda reservat només per configurar un publicador.
2. A la configuració de Trusted Publishers del projecte PyPI, registra GitHub Actions amb:
   - Owner: `mnebot`
   - Repository: `mina`
   - Workflow: `candidate.yml`
   - Environment: buit (el workflow no utilitza un GitHub Environment).
3. Registra un segon Trusted Publisher amb el mateix owner i repositori, però amb el workflow `stable.yml` i sense environment. Aquest publicador només s'utilitza en la promoció manual d'un candidat que hagi passat la validació a totes les Pi.
4. Comprova que GitHub Actions està habilitat per al repositori i que el workflow `CI` és obligatori per als canvis a `master`. La publicació de candidats només s'executa quan el workflow `CI` acaba correctament per un `push` a `master`.
5. Mantén activada la protecció de `master`; els workflows recuperen i construeixen exactament el commit validat per `CI`.

La publicació utilitza OIDC (`id-token: write`) i PyPI Trusted Publishing. No cal crear ni emmagatzemar un token d'API de PyPI a GitHub Secrets. Els workflows consulten PyPI abans de pujar: un reintent només s'omet si el wheel publicat té el mateix SHA-256; si el contingut difereix, la publicació falla sense sobreescriure la versió.

## Configurar les Raspberry Pi

Desa aquestes dades com a secrets protegits del repositori GitHub; no les afegeixis al repositori ni als logs:

- `MINA_TARGETS_JSON`: objecte JSON amb una llista no buida de dispositius. Cada dispositiu té un `alias` únic en minúscules, `host` (nom DNS del tailnet o IP) i `user` (compte Linux no-root), per exemple:

  ```json
  {"devices":[{"alias":"pi-cuina","host":"mina-cuina.<tailnet>.ts.net","user":"mina-deploy"}]}
  ```

- `TAILSCALE_OAUTH_CLIENT_ID` i `TAILSCALE_OAUTH_SECRET`: credencials d'un client OAuth de Tailscale limitat a l'etiqueta de runner (per exemple, `tag:github-actions`). Configura les ACL perquè aquest runner només pugui arribar als dispositius de desplegament i assigna-li el mínim privilegi necessari.

Prepara cada Pi una sola vegada com a administrador:

1. Crea el compte Linux `mina-deploy` i activa Tailscale SSH al dispositiu amb `tailscale set --ssh`.
2. Des del checkout del repositori al dispositiu, instal·la els fitxers bootstrap com a root:

   ```sh
   install -d -o root -g root -m 0755 /usr/local/lib/mina-deploy/scripts /usr/local/lib/mina-deploy/systemd
   install -o root -g root -m 0750 scripts/install_systemd_service.sh /usr/local/lib/mina-deploy/scripts/
   install -o root -g root -m 0750 scripts/deploy_remote.sh /usr/local/lib/mina-deploy/scripts/
   install -o root -g root -m 0644 systemd/mina.service /usr/local/lib/mina-deploy/systemd/
   ln -s /usr/local/lib/mina-deploy/scripts/deploy_remote.sh /usr/local/sbin/mina-deploy-candidate
   ```

   Mantén tots aquests fitxers root-owned i no modificables pel compte `mina-deploy`; actualitza'ls manualment quan canviï el helper.
3. Amb `visudo -f /etc/sudoers.d/mina-deploy`, afegeix `mina-deploy ALL=(root) NOPASSWD: /usr/local/sbin/mina-deploy-candidate *` i protegeix el fitxer amb mode `0440`. El helper valida la versió i només accepta prereleases.
4. A la política SSH de Tailscale, permet `tag:github-actions` connectar-se als dispositius Pi com a usuari `mina-deploy`; limita els dispositius amb tags i les ACL del tailnet.

En cada desplegament, el helper comprova si existeix `mina.service`; si falta, utilitza els fitxers root-owned per instal·lar el servei systemd, crear el compte runtime no privilegiat `mina`, configurar el socket i habilitar el servei abans d'instal·lar el candidat. Després atura el servei, instal·la el candidat al Python del dispositiu, canvia l'enllaç de versió, reinicia i comprova la versió i la resposta CLI. Cada Pi també necessita accés sortint HTTPS a PyPI.

El workflow valida l'inventari abans de connectar-se; un inventari absent, buit o invàlid falla sense iniciar cap connexió. La connexió usa Tailscale SSH i no necessita cap clau SSH privada ni `known_hosts` a GitHub Secrets. Els logs complets es conserven a `/var/log/mina/deploy.log` i `/var/log/mina/service.log`; els artefactes públics només identifiquen dispositius pel seu àlies, mai pel nom DNS ni per l'adreça real. Protegeix `master` i limita qui pot executar workflows perquè els secrets només s'utilitzin amb codi revisat.

## Promoció estable

Quan totes les Pi hagin validat el candidat, inicia manualment la pipeline de promoció per al commit provat. Aquesta publica la versió estable base (per exemple `0.1.1`), crea el tag `v0.1.1` i una GitHub Release amb els enllaços i les instruccions per als usuaris.

Per iniciar la promoció, executa manualment `Promote stable release` a la branca `master` i indica l'ID del run de `Publish candidate`. El workflow rebutja runs fallits/desconeguts o sense un resultat de desplegament exitós per a tots els dispositius. La creació del tag només publica la release estable; els desplegaments a les Pi continuen activant-se pels candidats validats després dels merges a `master`, no pel tag estable.

Instal·lació d'una versió estable concreta:

```sh
python -m pip install mina-voice-assistant==0.1.1
```

Després de la promoció, la primera PR del cicle següent incrementa la versió base de `pyproject.toml` una vegada més.
