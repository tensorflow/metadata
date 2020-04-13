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

load("@org_tensorflow//tensorflow/core/platform:default/build_config.bzl", "tf_proto_library_cc", "tf_proto_library_py")


tf_proto_library_cc(
    # TF generates rule with name cc_metadata_v0_proto_cc
    name = "cc_metadata_v0_proto",
    srcs = [
        "anomalies.proto",
        "metric.proto",
        "path.proto",
        "problem_statement.proto",
        "schema.proto",
        "statistics.proto",
    ]
)

cc_library(
    name = "metadata_v0_proto_cc_pb2",
    deps = [":cc_metadata_v0_proto_cc"],
)

tf_proto_library_py(
    # TF generates rule with name py_metadata_v0_proto_py
    name = "py_metadata_v0_proto",
    srcs = [
        "anomalies.proto",
        "metric.proto",
        "path.proto",
        "problem_statement.proto",
        "schema.proto",
        "statistics.proto",
    ],
)

py_library(
    name = "metadata_v0_proto_py_pb2",
    deps = [":py_metadata_v0_proto_py"],
)

