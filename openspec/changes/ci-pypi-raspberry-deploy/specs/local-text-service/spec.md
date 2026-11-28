# Spec Delta

## Purpose

Provides a lightweight resident service and local command-line interface for submitting text to Mina's core and receiving its response.

## ADDED Requirements

### Requirement: The text service remains available as a managed process
The Mina runtime SHALL run as a resident Linux service that can be started, stopped, and restarted by the operating system service manager.

#### Scenario: The service starts successfully
- **WHEN** the Mina service is started
- **THEN** it becomes ready to accept local text requests and remains available between requests

#### Scenario: The service is restarted
- **WHEN** the service manager restarts Mina after an update
- **THEN** the service becomes ready again without requiring a hardware adapter

### Requirement: A local CLI submits text to the resident service
The CLI SHALL send a text request to the running service through a local-only inter-process channel and print the response returned by the core.

#### Scenario: A text request is submitted
- **WHEN** a user submits `encén el llum` through the CLI
- **THEN** the CLI prints `He rebut: encén el llum` from the resident service

#### Scenario: The service is unavailable
- **WHEN** the CLI cannot connect to the resident service
- **THEN** it reports the connection failure and exits unsuccessfully

### Requirement: The service does not expose a network listener
Text requests to the resident service SHALL be available only through local inter-process communication and SHALL NOT require a network port.

#### Scenario: A local client submits a request
- **WHEN** a CLI running on the same device connects to Mina
- **THEN** the request is handled without exposing a network listener

### Requirement: Logs omit submitted request contents
The service SHALL NOT write submitted text or response contents to operational logs.

#### Scenario: A request is processed
- **WHEN** the service logs request processing or an error
- **THEN** its operational log contains no submitted text or response content
