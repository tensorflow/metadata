# Version 1.11.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   Add a categorical indicator to the schema for `StringDomain`.
*   Add ProblemStatement Task.is_auxiliary field to allow specifying auxiliary
    tasks in multi-task learning problems.
*   Add the SequenceMetadata field to the schema to specify if this feature
    could be treated as a sequence feature.
*   Add a `CUSTOM_VALIDATION` Type in anomalies.proto.

## Breaking Changes

*  Histogram Buckets include their upper bound instead of their lower bound.

## Deprecations

*   N/A

