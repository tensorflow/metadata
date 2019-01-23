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

load("@protobuf_archive//:protobuf.bzl", "cc_proto_library", "py_proto_library")

cc_proto_library(
    name = "metadata_v0_proto_cc_pb2",
    srcs = [
        "anomalies.proto",
        "path.proto",
        "schema.proto",
        "statistics.proto",
    ],
    cc_libs = ["@protobuf_archive//:protobuf"],
    default_runtime = "@protobuf_archive//:protobuf",
    protoc = "@protobuf_archive//:protoc",
)

py_proto_library(
    name = "metadata_v0_proto_py_pb2",
    srcs = [
        "anomalies.proto",
        "path.proto",
        "schema.proto",
        "statistics.proto",
    ],
    default_runtime = "@protobuf_archive//:protobuf_python",
    protoc = "@protobuf_archive//:protoc",
    srcs_version = "PY2AND3",
    deps = ["@protobuf_archive//:protobuf_python"],
)

