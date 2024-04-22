# Version 1.15.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   Bump the Ubuntu version on which TFMD is tested to 20.04 (previously
    was 16.04).
*   Bumped the minimum bazel version required to build `tfmd` to 6.1.0.
*   Depends on `protobuf>=4.25.2,<5` for Python 3.11 and on 
    `protobuf>3.20.3,<4.21` for 3.9 and 3.10.
*   Depends on `googleapis-common-protos>=1.56.4,<2` for Python 3.11 and on
    `googleapis-common-protos>=1.52.0,<2` for 3.9 and 3.10.
*   Relax dependency on `absl-py` to include version 2.

## Breaking Changes

*   Removed `NaturalLanguageDomain.location_constraint_regex`.
    It was documented as "please do not use" and never implemented.

## Deprecations

*   Deprecated Python 3.8 support.

