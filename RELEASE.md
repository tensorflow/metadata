# Version 1.13.0

## Major Features and Improvements

*   Introduce `Schema.represent_variable_length_as_ragged` knob to automatically
    generate `RaggedTensor`s for variable length features.
*   Introduces a Schema option `HistogramSelection` to allow numeric drift/skew
    calculations to use QUANTILES histograms, which are more robust to outliers.

## Bug Fixes and Other Changes

*   N/A

## Breaking Changes

*   N/A

## Deprecations

*   Deprecated Python 3.7 support.

