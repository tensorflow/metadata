# Copyright 2025 The TensorFlow Authors. All Rights Reserved.
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


load("@com_google_protobuf//bazel:py_proto_library.bzl", "py_proto_library")

licenses(["notice"])  # Apache 2.0

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "metadata_v0_proto",
    srcs = [
        "anomalies.proto",
        "derived_feature.proto",
        "metric.proto",
        "path.proto",
        "problem_statement.proto",
        "schema.proto",
        "statistics.proto",
    ],
    deps = [
        # For well-known proto types like protobuf.Any.
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:api_proto",
        "@com_google_protobuf//:compiler_plugin_proto",
        "@com_google_protobuf//:descriptor_proto",
        "@com_google_protobuf//:duration_proto",
        "@com_google_protobuf//:empty_proto",
        "@com_google_protobuf//:field_mask_proto",
        "@com_google_protobuf//:source_context_proto",
        "@com_google_protobuf//:struct_proto",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:type_proto",
        "@com_google_protobuf//:wrappers_proto",
    ],
)

cc_proto_library(
    name = "cc_metadata_v0_proto_cc",
    deps = [
        ":metadata_v0_proto",
    ],
)

cc_library(
    name = "metadata_v0_proto_cc_pb2",
    deps = [":cc_metadata_v0_proto_cc"],
)

py_proto_library(
    name = "metadata_v0_proto_py_pb2",
    deps = [
        ":metadata_v0_proto",
    ],
)

