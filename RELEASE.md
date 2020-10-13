<!-- mdlint off(HEADERS_TOO_MANY_H1) -->
# Current version (not yet released; still in development)

## Major Features and Improvements

* Added new Anomaly and Schema field to support drift and distribution skew
  detection for numeric features.
* Added a new field in Anomalies proto to report the raw measurements of
  distribution skew detection.

## Bug Fixes and Other Changes

* Added new Anomaly type to describe when a domain is incompatible with the
  data type.
* Added new Anomaly types for invalid schema configurations (missing name,
  missing type, etc).
* Added new Anomaly type to describe when type does not match the data.

## Breaking changes

## Deprecations

# Version 0.24.0

## Major Features and Improvements

*   From this version we will be releasing python 3.8 wheels.

## Bug Fixes and Other Changes

*   When installing from source, you don't need any steps other than
    `pip install` (needs Bazel).
*   Labels can be specified as Paths in addition to string names.
*   Depends on `absl-py>=0.9,<0.11`.
*   Depends on `googleapis-common-protos>=1.52.0,<2`.

## Breaking changes

*   N/A

## Deprecations

*   Deprecated Python 3.5 support.

# Version 0.23.0

## Major Features and Improvements

* Added disallow_inf to FloatDomain message in schema.proto.
* Added new Anomaly type to describe data that has unexpected Infs / -Infs.
* Added new Anomaly and Schema field for specifying ratio of supported images.
* Added value_counts field to Feature message in schema.proto, which describes
  the number of values for features that have more than one nestedness level.
* Added new anomaly type VALUE_NESTEDNESS_MISMATCH to describe data that has a
  nestedness level that does not match the schema.
* Added new Any type value to CustomStatistic.

## Bug Fixes and Other Changes

* Add ProblemStatement and Metric Python proto stubs.
* Use absltest instead of unittest.

## Breaking changes

* N/A

## Deprecations

* Drops Python 2 support.
* Note: We plan to remove Python 3.5 support after this release.

# Version 0.22.2

## Major Features and Improvements

* Added UniqueConstraints to Feature message in schema.proto.
* Added new Anomaly types to describe data that does not conform to
  UniqueConstraints.
* Added PresenceAndValencyStatistics to CommonStatistics.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.22.1

## Major Features and Improvements

* Added RaggedTensor in TensorRepresentation

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.22.0

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added a new type of Anomaly: DATASET_HIGH_NUM_EXAMPLES
* Added a new field to dataset_constraints: max_examples_count
* Added a multi-label TaskType.
* Removed ProblemStatementNamespace proto
* Removed ProblemStatementReference proto
* Removed field ProblemStatement.implements

## Breaking Changes

## Deprecations

# Version 0.21.2

## Major Features and Improvements

## Bug Fixes and Other Changes

* Fixed a compatibility issue with newer bazel versions.
* Started pulling TF 1.15.2 source for building.

## Breaking Changes

## Deprecations

# Version 0.21.1

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added support for specifying behavior of rare / OOV multiclass labels.
* Added anomaly types related to weighted features.
* Added support for storing lift stats on weighted examples.

## Breaking changes

* The removal of `lift_series` from `CategoricalCrossStats` and the change of
  type of `LiftSeries.LiftValue.lift` from float to double will cause parsing
  failures for serialized protos written written by version 0.21.0 which
  contained the deleted or changed fields.

## Deprecations

# Version 0.21.0

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added protos for categorical cross statistics using lift.
* Added a new type of Anomaly: FLOAT_TYPE_HAS_NAN
* Added a new field to float_domain: disallow_nans

## Breaking Changes

## Deprecations

# Version 0.15.2

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added SparseTensor to TensorRepresentation.
* Added a new type of Anomaly

## Breaking Changes

## Deprecations


# Version 0.15.1

## Bug Fixes and Other Changes

* Add WeightedFeature to schema.
* Add min_examples_count to DatasetConstraints and DATASET_LOW_NUM_EXAMPLES
  anomaly type.
* Add TimeOfDay domain and UNIX_DAY granularity for TimeDomain in schema.
* Added TensorRepresentation to schema.

# Version 0.15.0

No significant changes. Upgrading to keep version alignment.

## Major Features and Improvements

## Bug Fixes and Other Changes

* Adding CustomMetric to PerformanceMetric.

## Breaking changes

## Deprecations

# Version 0.14.0

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added an Any field to Schema Feature, for storing arbitrary structured
data.

## Breaking changes

* Refactoring ProblemStatement and related protos. At present, these are not 
stable.

## Deprecations

# Version 0.13.0

## Major Features and Improvements

* Added ProblemStatement.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.12.0

## Major Features and Improvements

* Add support for declaring sparse features.
* Add support for schema diff regions.

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.9.0

## Major Features and Improvements

* Adding functionality for handling structured data.

## Bug Fixes and Other Changes

* StructStatistics.common_statistics changed to
  StructStatistics.common_stats to agree with Facets.

## Breaking changes

* The change from StructStatistics.common_statistics to 
  StructStatistics.common_stats may break code that had this field set and
  was serializing to some text format. The wire format should be fine.

# Version 0.6.0

## Major Features and Improvements

* Use the same version of protobuf as tensorflow.
* Added support for structural statistics.
* Added new error types.
* Removed DiffRegion.
* added RankHistogram to CustomStatistics.

## Bug Fixes and Other Changes

## Breaking changes

* Removed DiffRegion.

# Version 0.5.0

## Major Features and Improvements

* Established tf.Metadata as a standalone package.

## Bug Fixes and Other Changes

## Breaking changes

* Moved tf.Metadata code out of TF-Transform code tree, requiring package
  dependency updates and import updates.
