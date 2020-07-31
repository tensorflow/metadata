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
"""Tests for tensorflow_metadata.python.proto."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
from tensorflow_metadata.proto.v0 import schema_pb2


class ProtoTest(absltest.TestCase):

  def test_import_works(self):
    """Checks that the import of the tensorflow_metadata module works."""
    # pylint:disable=unused-variable
    # We don't explicitly check all the symbols we know about now, because we
    # don't want to have to keep this test in sync with changes to the
    # underlying library.
    # Check for the presence of the Schema symbol.
    dummy = schema_pb2.Schema
    del dummy


if __name__ == '__main__':
  absltest.main()
