#!/bin/bash
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Moves the bazel generated files needed for packaging the wheel to the source
# tree.

function _is_windows() {
  [[ "$(uname -s | tr 'A-Z' 'a-z')" =~ (cygwin|mingw32|mingw64|msys)_nt* ]]
}

function tfmd::move_generated_files() {
  set -eux
  if _is_windows; then
    # Newer bazel does not create bazel-genfiles any more (
    # https://github.com/bazelbuild/bazel/issues/6761). It's merged with bazel-bin
    GENFILES=bazel-genfiles
    if [[ ! -d ${BUILD_WORKSPACE_DIRECTORY}/${GENFILES} ]]; then
      GENFILES=bazel-bin
    fi
    for f in ${BUILD_WORKSPACE_DIRECTORY}/${GENFILES}/tensorflow_metadata/proto/v0/*.py
    do
      cp -f "$f" \
      ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0
    done
  else
    for f in tensorflow_metadata/proto/v0/*.py
    do
      cp -f "$f" \
        ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0
    done
  fi
}

tfmd::move_generated_files
