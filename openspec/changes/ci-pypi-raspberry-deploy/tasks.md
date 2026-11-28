# Tasks

## 1. Package identity and versioning

- [x] 1.1 Rename the distribution metadata to `mina-voice-assistant` while preserving the `mina` import package; verify wheel metadata and the existing package-import test.
- [x] 1.2 Add unique `x.y.z.devN` candidate version generation from the next stable base version; test PEP 440 parsing, uniqueness across merge runs, and safe retries of an already-published candidate.
- [x] 1.3 Document how a PR advances the next stable base version and verify the documented sequence for candidate and stable versions.

## 2. Local text service

- [x] 2.1 Implement the resident core process and local CLI client over a Unix socket; add tests for the exact acknowledgement and for a clear non-zero failure when the service is unavailable.
- [ ] 2.2 Add the Linux service unit, unprivileged runtime account, and socket permissions; verify service startup, restart, and readiness on a Raspberry Pi.
- [x] 2.3 Ensure operational logs omit request and response text; add a regression test that checks log output contains no submitted text.

## 3. CI and candidate publication

- [x] 3.1 Add CI for pull requests and `master` changes that runs the existing regression subset, builds a wheel, and smoke-tests the installed wheel; verify CI fails when any check fails.
- [ ] 3.2 Add same-repository PR and master-push candidate publication using PyPI Trusted Publishing; verify each successful CI run gets a unique prerelease and failed/fork runs do not publish.
- [x] 3.3 Document the PyPI trusted-publisher and repository settings required for candidate publication; verify setup instructions without exposing credentials.

## 4. Raspberry Pi deployment

- [x] 4.1 Add protected PR-test and master deployment inventories plus Tailscale connection setup; test empty, malformed, and valid inventories and document the required GitHub/Tailscale configuration.
- [ ] 4.2 Implement per-device candidate deployment using the appropriate PR-test or master inventory and the device's installed Python/versioned environments; verify stop, install, service restart, installed version, and CLI response on a test Pi.
- [ ] 4.3 Add automatic rollback to the previous environment on update or smoke-check failure; test successful rollback and first-install failure behavior.
- [x] 4.4 Retain full logs on each Pi and upload only redacted failure diagnostics; verify the workflow identifies the artifact and on-device log path and that request text, secrets, and real device addresses are absent.
- [x] 4.5 Aggregate results across all configured devices and block stable promotion if any device fails; verify successful and partial-failure runs.
- [x] 4.6 Combine candidate publication and deployment in one workflow, separate unprivileged PR builds from privileged jobs, and verify fork PRs cannot publish or deploy.

## 5. Stable release and documentation

- [ ] 5.1 Add the manually dispatched stable promotion gated on successful master-candidate device validation; verify it builds the stable package from the revalidated master commit, publishes once, and rejects PR, failed, or unknown candidates.
- [ ] 5.2 Create the matching `vX.Y.Z` tag and GitHub Release with the exact install command and PyPI/documentation links; verify links resolve to the published version.

## 6. End-to-end verification

- [ ] 6.1 Exercise the merge-to-candidate-to-device-to-stable path on a controlled test target; verify the existing core regression subset, service update/rollback, manual promotion gate, and release documentation together.
