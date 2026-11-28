# Tasks

## 1. Python baseline and core ports

- [x] 1.1 Establish a minimal Python package and pytest layout; verify pytest discovers the test suite and imports the core package without optional integrations.
- [x] 1.2 Define explicit input and output port contracts for text requests and the `He rebut: <request>` acknowledgement, plus the minimal core request flow; add pytest cases proving the exact acknowledgement reaches the output port.
- [x] 1.3 Add a focused dependency-boundary test or equivalent check proving the core and port contracts can be imported without hardware, vendor SDK, or network/transport packages.

## 2. Documentation and validation

- [x] 2.1 Update section 4.1 of `docs/arquitectura.md` to identify the generic text input/output pair as the initial implementation and defer capability-specific ports to their respective backlog stories; verify the documentation matches the spec.
- [x] 2.2 Run the complete pytest suite and inspect runtime dependencies to confirm the core remains lightweight and has no external integration dependency.
