# Proposal

## Why

Mina has no automated validation, package release, or Raspberry Pi runtime update path. Add a release pipeline that validates each merge, exercises a prerelease on the target devices, and only promotes it to a stable, documented release after device checks and a deliberate manual release action.

## What Changes

- Add CI validation for pull requests and primary-branch changes, including the existing regression tests and a built-package smoke check.
- On a successful merge to `master`, publish a unique `x.y.z.devN` prerelease of the `mina-voice-assistant` distribution and automatically deploy it to every Raspberry Pi target configured in a protected GitHub secret.
- Add a resident `systemd` service and a CLI client that sends text over a local Unix socket and returns the existing core acknowledgement.
- Reach devices through Tailscale; stop the service, update the package with the device's installed Python, restart it, and verify both installed version and text response.
- After successful device checks, use a manually triggered release workflow as the approval to publish the stable version, create its version tag, and generate user-facing release notes with installation instructions and PyPI/documentation links.
- Preserve the Python import package name `mina`; hardware integrations such as audio and Hue remain out of scope.

## Capabilities

### New Capabilities

- `python-package-release`: Validate, build, and publish versioned Python package releases.
- `raspberry-pi-deployment`: Automatically deploy validated prereleases to configured Raspberry Pi devices and verify the running service.
- `local-text-service`: Run the core as a resident service that accepts text through a local CLI client and returns its response.

### Modified Capabilities

None. The existing core request/response contract remains unchanged.

## Impact

- Adds CI, prerelease deployment, and stable-release workflow configuration; updates Python distribution/version metadata without renaming the `mina` import package.
- Adds a CLI entry point and a Linux `systemd` service using the local core, without adding hardware-specific integrations.
- Requires PyPI trusted-publisher configuration for `mina-voice-assistant`, protected GitHub target configuration, and Tailscale access to the Pi devices.
- Reuses the existing pytest regression suite and verifies the deployed service's version and text request/response behavior.
