# Design

## Context

The repository currently contains project and architecture documentation but no application source or existing test suite. The architecture document selects Ports and Adapters and requires a lightweight core that can run on a Raspberry Pi 3. This change uses Python with pytest.

See `proposal.md` for the motivation and `specs/core-domain-and-intents/spec.md` for the required behavior.

## Goals / Non-Goals

**Goals:**
- Keep the initial boundary small: one input port for submitting a text request and one output port for returning a text outcome.
- Make the core and its contracts independent of concrete adapters and external integration packages.
- Leave later domain capabilities free to introduce their own explicit ports when those capabilities are implemented.

**Non-Goals:**
- Implement intent recognition, voice/audio processing, or any device or service integration.
- Define transport, serialization, concurrency, or persistence behavior not required by the current story.
- Introduce a plugin registry, dependency-injection framework, or other extensibility infrastructure.

## Decisions

- **Keep the contracts project-owned and define dependencies inward.** Input and output adapters depend on the port contracts; the core does not import adapter implementations. This preserves the architecture document's separation between orchestration/domain and hardware or provider details. A direct adapter-to-core implementation call was rejected because it couples adapters to replaceable internals.
- **Use one generic request path and one outcome path for this increment.** Do not create radio, Hue, Spotify, alarm, or audio ports yet; introduce those explicit capability ports with their corresponding backlog stories. This keeps US-02 minimal while retaining the ability to add capability-specific boundaries later. Defining every future port now was rejected as speculative scope.
- **Use text for the initial request and outcome, with a Catalan acknowledgement.** The core returns `He rebut: <request>` through the output port. This exercises the complete boundary without adding intent classification or domain-specific behavior.
- **Use Python and pytest without an application framework.** These are the selected implementation language and test runner. The contracts can be represented with standard-library types, avoiding dependencies added solely to express the ports.

## Risks / Trade-offs

- A generic text request/outcome pair may need refinement when the first real capability is added → keep the contracts small and evolve them alongside that capability's spec rather than predicting its payload now.
- Ports alone do not provide useful assistant behavior → keep behavior beyond the request/response boundary in later backlog stories.

## Migration Plan

There is no existing application code or runtime to migrate. Add the core and port contracts as a new baseline; rollback consists of removing that new implementation before downstream capabilities depend on it.

