# Version 0.12.0

## Major Features and Improvements

* Added ProblemStatement
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

# Version 0.9.0


## Bug Fixes and Other Changes

## Breaking changes

* Moved tf.Metadata code out of TF-Transform code tree, requiring package
  dependency updates and import updates.
