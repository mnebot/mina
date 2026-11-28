# Design

## Context

See `proposal.md` for the motivation and scope. The repository currently has a small `src/mina` package with a text core and ports, three pytest tests, no executable entry point, and no CI workflow. Its distribution metadata is currently named `mina` at version `0.1.0`; that PyPI name belongs to another project. The Python import package will remain `mina`, while the distribution will be `mina-voice-assistant`.

The repository is public. Device addresses and credentials therefore must not be committed. Raspberry Pi access is already provided by Tailscale, and each target may have a different installed Python version.

## Goals / Non-Goals

**Goals:**
- Keep the candidate package that is tested on devices tied to a specific merge commit and immutable prerelease version.
- Prevent a failed device update from leaving a previously working service down where rollback is possible.
- Keep requests local to the device and keep user-submitted text out of operational and uploaded diagnostic logs.
- Make stable publication and user-facing release notes a deliberate final action after device validation.

**Non-Goals:**
- Add audio, Hue, radio, Spotify, or other hardware adapters.
- Expose a network API for text requests.
- Publish stable versions automatically on every merge.

## Decisions

### Separate validation, candidate deployment, and stable promotion

Use three workflow phases:

1. **CI** runs on pull requests and changes to `master`; it runs the existing regression suite, builds the distribution, and smoke-tests an installation of the built wheel.
2. **Candidate distribution/deployment** runs after a successful merge to `master`. It derives a unique PEP 440 prerelease (`x.y.z.devN`) from the next stable version and the workflow run, publishes that exact candidate to PyPI, then deploys it to the configured Raspberry Pi devices. A candidate is not a stable release.
3. **Stable promotion** is a manually dispatched workflow after all configured devices pass. The dispatch is the manual approval. It rebuilds the same source commit with its stable `x.y.z` version, publishes it to PyPI, creates the matching `vX.Y.Z` tag, and creates a GitHub Release containing installation instructions and links to PyPI and documentation.

This keeps a single, immutable candidate version for device testing. A failed candidate is not overwritten; a later merge produces another unique prerelease. `pyproject.toml` must identify the next stable base version before its candidate is published. Retries must recognize an already-published candidate and verify/use that exact artifact rather than attempt to replace it.

Use PyPI Trusted Publishing/OIDC for publication instead of long-lived upload credentials. Before release, the owner must claim/configure `mina-voice-assistant` and its trusted publisher; availability should be rechecked because a 404 lookup is not a reservation.

### Keep the device inventory and access private

Store the JSON target inventory and access credentials in protected GitHub configuration, not in the public repository. The candidate workflow validates the inventory before connecting and deploys to all configured devices. It joins the existing Tailscale network and uses private device access; no public SSH port is required. Each device is reported independently, but any failed device blocks stable promotion.

### Run the core behind a local resident service

Keep the existing `Core` and its text ports as the application boundary. Add a resident process managed by `systemd` and a CLI client. The daemon accepts requests over a Unix-domain socket under `/run/mina`; the CLI submits text and prints the response. This avoids adding a network listener or a transport dependency and gives the deployment workflow a meaningful post-restart check.

The service runs as a dedicated unprivileged account. The CLI and service share only the socket contract; if the service is unavailable, the CLI exits unsuccessfully with a clear error. Operational logs record lifecycle and failures but never request or response text.

### Install candidates in versioned virtual environments

On each device, use its existing Python interpreter and a separate environment for each package version under `/opt/mina/versions/<version>`. The system service runs through `/opt/mina/current`. For an update, stop the service, create/install the candidate environment, switch the current-version pointer, and start the service. This preserves the previous environment for rollback without requiring another PyPI download.

On the first deployment, install the service configuration and candidate environment before starting the service. On an update failure, restore the previous pointer and restart the previous environment. If the first installation fails, report that there is no previous version to restore.

After startup, verify the installed distribution version and submit a known text request through the CLI, checking the exact core acknowledgement. The existing pytest cases remain CI regression tests; the device check validates the installed candidate rather than relying on source-tree imports.

### Keep failure details private while making them retrievable

Retain full deployment/service logs on the device under `/var/log/mina/`. The workflow result prints the target alias, on-device log path, and retrieval instructions. Upload only a redacted diagnostic artifact to GitHub Actions; omit request/response contents, secrets, and real device addresses. This gives maintainers a downloadable failure report without exposing user text or tailnet details through the public repository.

## Risks / Trade-offs

- **A candidate can be published before device testing succeeds** -> Keep it as a prerelease, deploy an exact version, and block stable promotion unless every configured device passes.
- **A configured device may be offline or incompatible with its installed Python** -> Report the affected target, keep stable promotion blocked, and test using that device's existing interpreter rather than silently upgrading Python.
- **The service or update may fail after stopping the old process** -> Preserve the previous versioned environment and restore it automatically; report rollback failure explicitly.
- **A failure log may contain sensitive text** -> The service never logs request content; upload only redacted diagnostics and retain full logs on-device.
- **PyPI versions and tags are immutable** -> Generate unique prereleases and stable tags; retries verify the existing artifact instead of replacing it.

## Migration Plan

1. Configure the PyPI trusted publisher and protected GitHub/Tailscale settings, including the private device inventory.
2. Release a candidate through the merge path and validate the first service installation on the configured devices.
3. After successful device checks, manually dispatch stable promotion for the tested commit; publish the stable version, create its tag, and publish its GitHub Release notes.
4. If stable promotion fails before publication, no stable tag is created. If a candidate update fails, restore the previous device environment where one exists and retain its diagnostics.
