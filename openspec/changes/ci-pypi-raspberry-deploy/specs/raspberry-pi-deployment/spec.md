# Spec Delta

## Purpose

Defines automatic deployment and verification of Mina prereleases on configured Raspberry Pi devices while protecting the running service and keeping failure diagnostics accessible.

## ADDED Requirements

### Requirement: Merged prereleases deploy to the configured devices
After a prerelease is published for a validated merge to `master`, the deployment flow SHALL automatically target every Raspberry Pi in the protected device inventory.

#### Scenario: A candidate and device inventory are available
- **WHEN** a validated prerelease is published and the protected inventory contains configured devices
- **THEN** deployment starts automatically for every device in that inventory

#### Scenario: The device inventory is missing or invalid
- **WHEN** deployment starts without a valid protected device inventory
- **THEN** it fails without attempting to connect to unconfigured devices and stable release promotion is blocked

### Requirement: Devices are reached through the private tailnet
The deployment flow SHALL reach devices through the configured Tailscale network and SHALL NOT require publicly exposed SSH access.

#### Scenario: A configured device is online
- **WHEN** the deployment flow connects to a configured device
- **THEN** it can manage the device without making its SSH service publicly reachable

### Requirement: The candidate is installed under a managed service
The deployment flow SHALL ensure a Mina system service exists, stop it before changing the installed candidate, and start it after the update using the device's installed Python interpreter.

#### Scenario: First deployment to a device
- **WHEN** a configured device has no Mina service
- **THEN** deployment installs the service configuration, installs the candidate, and starts the service

#### Scenario: Updating an existing service
- **WHEN** a configured device already runs Mina
- **THEN** deployment stops the service, installs the exact candidate version, and starts the service again

### Requirement: Device verification gates stable promotion
After the service starts, deployment SHALL verify the installed candidate version and the service's text request/response behavior on every configured device.

#### Scenario: Every device passes verification
- **WHEN** all configured devices report the requested candidate version and return the expected response to a text request
- **THEN** device validation succeeds and the candidate is eligible for stable release

#### Scenario: Any device fails verification
- **WHEN** installation, service startup, version verification, or the text request check fails on any device
- **THEN** device validation fails and stable release promotion is blocked

### Requirement: Failed updates restore the previous working version
If an update to an already configured device fails verification, deployment SHALL restore the previously installed package version and attempt to restart the service.

#### Scenario: An update fails after a previous version was running
- **WHEN** the candidate fails to install, start, or pass its smoke check
- **THEN** deployment attempts to restore the previous version and restart the service, and reports rollback success or failure

#### Scenario: First installation fails
- **WHEN** a device has no previous working Mina version and its first installation fails
- **THEN** deployment reports failure and does not report the service as healthy

### Requirement: Failure diagnostics are accessible without exposing request data
Deployment SHALL retain full device logs on the device, upload a redacted diagnostic artifact for failures, and identify the artifact and on-device log location in the workflow result.

#### Scenario: A device deployment fails
- **WHEN** deployment reports a device failure
- **THEN** the workflow result identifies the redacted diagnostic artifact and the device log location without including submitted request text or secrets

### Requirement: Hardware integrations are not required for candidate verification
Device verification SHALL exercise the installed service and text request/response contract without requiring audio, Hue, or other hardware adapters.

#### Scenario: A device has no assistant peripherals attached
- **WHEN** the candidate is deployed and verified without assistant peripherals
- **THEN** package, service, version, and text response checks can still complete
