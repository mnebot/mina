# Proposal

## Why

The project has an architectural direction but no implementation yet. A minimal, explicit boundary around a lightweight core lets the first increments add input and output adapters without binding the domain to hardware, vendor SDKs, or network transports.

## What Changes

- Define one minimal input port for submitting a text request to the core and one output port that returns the acknowledgement `He rebut: <request>`.
- Specify that the core depends only on project-owned contracts and remains independent of ALSA, third-party SDKs, and transport/network details.
- Keep this increment limited to the port-and-core boundary; intent classification and concrete audio, Hue, radio, Spotify, alarm, and timer integrations remain out of scope.

## Capabilities

### New Capabilities

- `core-domain-and-intents`: Establish the minimal core boundary and its input/output port contracts as a foundation for later capabilities.

### Modified Capabilities

None.

## Impact

- Adds a new OpenSpec capability; there are no existing source modules or tests to extend.
- Uses Python for the implementation and pytest for verification, as selected for this change.
- Defines project-owned contracts for a minimal request path and response path. No external runtime, hardware, vendor SDK, or network dependency is introduced by this change.
- Provides a foundation for subsequent backlog stories without implementing their behavior.
