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

licenses(["notice"])  # Apache 2.0

package(default_visibility = ["//visibility:public"])

load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

METADATA_PROTO_SRCS = [
    "anomalies.proto",
    "path.proto",
    "schema.proto",
    "statistics.proto",
]

proto_library(
    name = "metadata_v0_proto",
    srcs = METADATA_PROTO_SRCS,
)

cc_proto_library(
    name = "metadata_v0_proto_cc_pb2",
    deps = [":metadata_v0_proto"],
)

py_proto_library(
    name = "metadata_v0_proto_py_pb2",
    srcs = METADATA_PROTO_SRCS,
    srcs_version = "PY2AND3",
)

java_proto_library(
    name = "metadata_v0_proto_java_pb2",
    deps = [":metadata_v0_proto"],
)
