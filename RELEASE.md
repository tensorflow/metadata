# Version 1.6.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   statistics.proto: Includes a field `invalid_utf8_count` in `StringStatistics`
    to store the number of non-utf8 encoded strings for a feature.
*   Depends on `absl-py>=0.9,<2.0.0`.

## Breaking Changes

*   Removes deprecated field `objective_function` from ProblemStatement.

## Deprecations

*   Deprecates `multi_objective` field in ProblemStatement.
*   Deprecates several unused PerformanceMetrics.

