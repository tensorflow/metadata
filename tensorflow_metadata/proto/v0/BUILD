# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


load("@com_google_protobuf//:protobuf.bzl", "cc_proto_library", "py_proto_library")

licenses(["notice"])  # Apache 2.0

package(default_visibility = ["//visibility:public"])


cc_proto_library(
    name = "cc_metadata_v0_proto_cc",
    srcs = [
        "anomalies.proto",
        "metric.proto",
        "path.proto",
        "problem_statement.proto",
        "schema.proto",
        "statistics.proto",
        "derived_feature.proto",
    ],
    deps = [
        # For well-known proto types like protobuf.Any.
        "@com_google_protobuf//:cc_wkt_protos",
    ],
)

cc_library(
    name = "metadata_v0_proto_cc_pb2",
    deps = [":cc_metadata_v0_proto_cc"],
)

py_proto_library(
    name = "py_metadata_v0_proto_py",
    srcs = [
        "anomalies.proto",
        "metric.proto",
        "path.proto",
        "problem_statement.proto",
        "schema.proto",
        "statistics.proto",
        "derived_feature.proto",
    ],
    deps = [
        # For well-known proto types like protobuf.Any.
        "@com_google_protobuf//:well_known_types_py_pb2",
    ],
)

py_library(
    name = "metadata_v0_proto_py_pb2",
    deps = [":py_metadata_v0_proto_py"],
)

