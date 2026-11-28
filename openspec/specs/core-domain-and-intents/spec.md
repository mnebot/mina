# core-domain-and-intents Specification

## Purpose

Defines the lightweight core boundary that accepts a request and returns an outcome through explicit ports. This capability gives future input and output adapters a stable seam without taking on domain-specific integrations.

## Requirements

### Requirement: Core accepts requests through an explicit input port
The system SHALL provide one explicit, project-owned input contract through which an input adapter can submit a text request to the core without depending on a concrete core implementation.

#### Scenario: An adapter submits a request
- **WHEN** an input adapter submits a text request through the input contract
- **THEN** the core receives that request without the adapter needing to know the core's concrete implementation

### Requirement: Core returns outcomes through an explicit output port
The system SHALL provide one explicit, project-owned output contract through which the core makes the acknowledgement `He rebut: <request>` available for each submitted text request, without prescribing a hardware or transport delivery mechanism.

#### Scenario: The core returns a request outcome
- **WHEN** the core receives the text request `encén el llum`
- **THEN** it makes the text `He rebut: encén el llum` available through the output contract for an output adapter to deliver

### Requirement: Core remains independent of external integration details
The core and its port contracts SHALL NOT require dependencies on hardware libraries, third-party vendor SDKs, or network and transport implementations.

#### Scenario: A concrete adapter is not present
- **WHEN** the core is built or exercised without a hardware, vendor, or transport adapter
- **THEN** the core and its port contracts remain usable without those external integration dependencies
