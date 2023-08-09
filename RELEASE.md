# Version 1.14.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes
*   Add `joint_group` to `SequenceMetadata` to specify which group this sequence
    feature belongs to so that they can be modeled jointly.
*   Add `BOOL_TYPE_INVALID_CONFIG` anomaly type.
*   Add `embedding_dim` to `FloatDomain` to specify the embedding dimension,
    which is useful for use cases such as restoring shapes for flattened
    sequence of embeddings.
*   Add `sequence_truncation_limit` to `SequenceMetadata` to specify the maximum
    sequence length that should be processed.
*   Depends on `protobuf>=3.20.3,<4.21`. Upper bound is required to avoid
    breaking changes.

## Breaking Changes

*   N/A

## Deprecations

*   N/A

