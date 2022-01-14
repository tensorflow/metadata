<!-- mdlint off(HEADERS_TOO_MANY_H1) -->

# Current Version (not yet released; still in development)

## Major Features and Improvements

## Bug Fixes and Other Changes

*  statistics.proto: Includes a field `invalid_utf8_count` in `StringStatistics`
   to store the number of non-utf8 encoded strings for a feature.

## Breaking Changes

*   Removes deprecated field `objective_function` from ProblemStatement.

## Deprecations

*   Deprecates `multi_objective` field in ProblemStatement.
*   Deprecates several unused PerformanceMetrics

# Version 1.5.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   A `threshold_config` is added to MetaOptimizationTarget to allow for
    expressing thresholded optimization goals.

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 1.4.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   Added a new field to `FloatDomain` in schema to allow expression of
    categorical floats.

## Breaking Changes

*   N/A

## Deprecations

*   Deprecated Python 3.6 support.

# Version 1.3.x (skipped)

*  To maintain version consistency among TFX Family libraries we skipped
   the 1.3.x release for TFMD library.

# Version 1.2.0

## Major Features and Improvements

*   Added `PositiveNegativeSpec` to `ProblemStatement.BinaryClassification` for
    specifying positive and negative class values.

## Bug Fixes and Other Changes

*   N/A

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 1.1.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*   Depends on `protobuf>=3.13,<4`.

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 1.0.0

## Major Features and Improvements

*  Added public python interface for proto/* in proto/__init__.py

## Bug Fixes and Other Changes

*   N/A

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 0.30.0

## Major Features and Improvements

*   N/A

## Bug Fixes and Other Changes

*  Added new anomaly types: `MULTIPLE_REASONS` and
   `INVALID_DOMAIN_SPECIFICATION`.
*  Added new anomaly type: `STATS_NOT_AVAILABLE`.

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 0.29.0

## Major Features and Improvements

*   Adding the ability to specify and detect sequence length issues.

## Bug Fixes and Other Changes

*   Depends on `absl-py>=0.9,<0.13`.

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 0.28.0

## Major Features and Improvements

*   Added new anomaly type `MAX_IMAGE_BYTE_SIZE_EXCEEDED` for image_domain.
*   Added new anomaly type `INVALID_FEATURE_SHAPE`.
*   The `RaggedTensor` TensorRepresentation now supports additional partitions.

## Bug Fixes and Other Changes

*   N/A

## Breaking Changes

*   N/A

## Deprecations

*   N/A

# Version 0.27.0

## Major Features and Improvements

*   Added new anomaly types to AnamalyInfo to report data issues with NL
    features.

## Bug Fixes and Other Changes

*   Added new FloatDomain field and anomaly type to designate and validate
    features that represent fixed dimensional embeddings.

## Breaking changes

*   N/A

## Deprecations

*   N/A

# Version 0.26.0

## Major Features and Improvements

*   Added new fields to NaturalLanguageDomain message in the schema, including
    support for specifying vocabularies, constriants on sequence values
    (SequenceValueConstraints), constraints on vocabulary coverage
    (FeatureCoverageConstraints), and constraints on token location
    (location_constraints_regex).
*   Added new NaturalLanguageStatistics message to the statistics.proto so that
    we can compute statistics corresponding to Natural Language features.

## Bug Fixes and Other Changes

*   N/A

## Breaking changes

*   N/A

## Deprecations

*   N/A

# Version 0.25.0

## Major Features and Improvements

*   Added new Anomaly and Schema field to support drift and distribution skew
    detection for numeric features.
*   Added a new field in Anomalies proto to report the raw measurements of
    distribution skew detection.
*   From this release TFMD will also be hosting nightly packages on
    https://pypi-nightly.tensorflow.org. To install the nightly package use the
    following command:

    ```
    pip install -i https://pypi-nightly.tensorflow.org/simple tensorflow-metadata
    ```

    Note: These nightly packages are unstable and breakages are likely to
    happen. The fix could often take a week or more depending on the complexity
    involved for the wheels to be available on the PyPI cloud service. You can
    always use the stable version of TFMD available on PyPI by running the
    command `pip install tensorflow-metadata` .

## Bug Fixes and Other Changes

*   Added new Anomaly type to describe when a domain is incompatible with the
    data type.
*   Added new Anomaly types for invalid schema configurations (missing name,
    missing type, etc).
*   Added new Anomaly type to describe when type does not match the data.
*   Added new LifecycleStage:DISABLED.

## Breaking changes

*   N/A

## Deprecations

*   N/A

# Version 0.24.0

## Major Features and Improvements

*   From this version we will be releasing python 3.8 wheels.

## Bug Fixes and Other Changes

*   When installing from source, you don't need any steps other than `pip
    install` (needs Bazel).
*   Labels can be specified as Paths in addition to string names.
*   Depends on `absl-py>=0.9,<0.11`.
*   Depends on `googleapis-common-protos>=1.52.0,<2`.

## Breaking changes

*   N/A

## Deprecations

*   Deprecated Python 3.5 support.

# Version 0.23.0

## Major Features and Improvements

*   Added disallow_inf to FloatDomain message in schema.proto.
*   Added new Anomaly type to describe data that has unexpected Infs / -Infs.
*   Added new Anomaly and Schema field for specifying ratio of supported images.
*   Added value_counts field to Feature message in schema.proto, which describes
    the number of values for features that have more than one nestedness level.
*   Added new anomaly type VALUE_NESTEDNESS_MISMATCH to describe data that has a
    nestedness level that does not match the schema.
*   Added new Any type value to CustomStatistic.

## Bug Fixes and Other Changes

*   Add ProblemStatement and Metric Python proto stubs.
*   Use absltest instead of unittest.

## Breaking changes

*   N/A

## Deprecations

*   Drops Python 2 support.
*   Note: We plan to remove Python 3.5 support after this release.

# Version 0.22.2

## Major Features and Improvements

*   Added UniqueConstraints to Feature message in schema.proto.
*   Added new Anomaly types to describe data that does not conform to
    UniqueConstraints.
*   Added PresenceAndValencyStatistics to CommonStatistics.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.22.1

## Major Features and Improvements

*   Added RaggedTensor in TensorRepresentation

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.22.0

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Added a new type of Anomaly: DATASET_HIGH_NUM_EXAMPLES
*   Added a new field to dataset_constraints: max_examples_count
*   Added a multi-label TaskType.
*   Removed ProblemStatementNamespace proto
*   Removed ProblemStatementReference proto
*   Removed field ProblemStatement.implements

## Breaking Changes

## Deprecations

# Version 0.21.2

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Fixed a compatibility issue with newer bazel versions.
*   Started pulling TF 1.15.2 source for building.

## Breaking Changes

## Deprecations

# Version 0.21.1

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Added support for specifying behavior of rare / OOV multiclass labels.
*   Added anomaly types related to weighted features.
*   Added support for storing lift stats on weighted examples.

## Breaking changes

*   The removal of `lift_series` from `CategoricalCrossStats` and the change of
    type of `LiftSeries.LiftValue.lift` from float to double will cause parsing
    failures for serialized protos written written by version 0.21.0 which
    contained the deleted or changed fields.

## Deprecations

# Version 0.21.0

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Added protos for categorical cross statistics using lift.
*   Added a new type of Anomaly: FLOAT_TYPE_HAS_NAN
*   Added a new field to float_domain: disallow_nans

## Breaking Changes

## Deprecations

# Version 0.15.2

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Added SparseTensor to TensorRepresentation.
*   Added a new type of Anomaly

## Breaking Changes

## Deprecations

# Version 0.15.1

## Bug Fixes and Other Changes

*   Add WeightedFeature to schema.
*   Add min_examples_count to DatasetConstraints and DATASET_LOW_NUM_EXAMPLES
    anomaly type.
*   Add TimeOfDay domain and UNIX_DAY granularity for TimeDomain in schema.
*   Added TensorRepresentation to schema.

# Version 0.15.0

No significant changes. Upgrading to keep version alignment.

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Adding CustomMetric to PerformanceMetric.

## Breaking changes

## Deprecations

# Version 0.14.0

## Major Features and Improvements

## Bug Fixes and Other Changes

*   Added an Any field to Schema Feature, for storing arbitrary structured data.

## Breaking changes

*   Refactoring ProblemStatement and related protos. At present, these are not
    stable.

## Deprecations

# Version 0.13.0

## Major Features and Improvements

*   Added ProblemStatement.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.12.0

## Major Features and Improvements

*   Add support for declaring sparse features.
*   Add support for schema diff regions.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.9.0

## Major Features and Improvements

*   Adding functionality for handling structured data.

## Bug Fixes and Other Changes

*   StructStatistics.common_statistics changed to StructStatistics.common_stats
    to agree with Facets.

## Breaking changes

*   The change from StructStatistics.common_statistics to
    StructStatistics.common_stats may break code that had this field set and was
    serializing to some text format. The wire format should be fine.

# Version 0.6.0

## Major Features and Improvements

*   Use the same version of protobuf as tensorflow.
*   Added support for structural statistics.
*   Added new error types.
*   Removed DiffRegion.
*   added RankHistogram to CustomStatistics.

## Bug Fixes and Other Changes

## Breaking changes

*   Removed DiffRegion.

# Version 0.5.0

## Major Features and Improvements

*   Established tf.Metadata as a standalone package.

## Bug Fixes and Other Changes

## Breaking changes

*   Moved tf.Metadata code out of TF-Transform code tree, requiring package
    dependency updates and import updates.
