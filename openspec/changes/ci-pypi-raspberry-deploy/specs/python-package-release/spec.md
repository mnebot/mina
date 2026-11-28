# Spec Delta

## Purpose

Defines repeatable validation and staged publication of Mina's Python distribution so merged changes can be tested on target devices before a stable release is promoted.

## ADDED Requirements

### Requirement: Pull requests and primary-branch changes are validated
CI SHALL run the existing core regression suite and verify that the Python distribution can be built and imported from the built package.

#### Scenario: All checks pass
- **WHEN** a pull request or change to `master` is checked
- **THEN** CI reports success only after the regression suite, package build, and built-package smoke check pass

#### Scenario: A check fails
- **WHEN** any regression, build, or built-package smoke check fails
- **THEN** CI reports failure and no candidate is eligible for publication or deployment

### Requirement: The published distribution has a distinct PyPI name
The Python distribution published to PyPI SHALL be named `mina-voice-assistant` and SHALL continue to provide the `mina` import package.

#### Scenario: A user installs the distribution
- **WHEN** a user installs `mina-voice-assistant`
- **THEN** the installed package can be imported as `mina`

### Requirement: Validated same-repository changes publish unique prereleases
After successful CI for a same-repository pull request or a push to `master`, the release flow SHALL publish a unique prerelease version based on the next stable version. Fork pull requests SHALL NOT receive PyPI publishing permissions.

#### Scenario: Same-repository pull request passes CI
- **WHEN** a same-repository pull request targeting `master` passes CI
- **THEN** a unique `x.y.z.devN` version of `mina-voice-assistant` is published to PyPI for test-device validation

#### Scenario: A validated change is merged
- **WHEN** a push to `master` passes CI
- **THEN** a unique `x.y.z.devN` version of `mina-voice-assistant` is published to PyPI for deployment-device validation

#### Scenario: CI validation fails
- **WHEN** the candidate-triggering CI run does not pass its required validation
- **THEN** no prerelease is published

#### Scenario: A fork pull request passes CI
- **WHEN** a pull request from a fork passes CI
- **THEN** no PyPI publishing or device-deployment job receives credentials or runs

### Requirement: Stable releases require a successful master candidate and manual dispatch
The release flow SHALL publish a stable version and create its matching version tag only after a candidate built from a successful `master` push passes device validation and an operator manually dispatches the release. A PR candidate SHALL NOT be promotable.

#### Scenario: The candidate passes and release is manually dispatched
- **WHEN** device validation succeeds for a candidate and the operator manually dispatches its stable release
- **THEN** the matching `x.y.z` version is published to PyPI and a `vX.Y.Z` tag is created for the candidate's source commit

#### Scenario: Candidate validation fails or release is not dispatched
- **WHEN** device validation fails or no manual release dispatch occurs
- **THEN** no stable version or release tag is created

### Requirement: Stable tags provide installation documentation
Each stable version tag SHALL have user-facing release information that identifies the PyPI package, links to the published version and documentation, and explains how to install that version.

#### Scenario: A user opens a stable release
- **WHEN** a user views the GitHub release associated with a stable tag
- **THEN** the release provides the exact `pip` installation command and links to the PyPI version and relevant documentation
