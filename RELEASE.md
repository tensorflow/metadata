# Current version (not yet released; still in development)

## Major Features and Improvements

## Bug Fixes and Other Changes

## Breaking changes

## Deprecations

# Version 0.21.0

## Major Features and Improvements

## Bug Fixes and Other Changes

* Added protos for categorical cross statistics using lift.

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
