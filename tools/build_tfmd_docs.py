# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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
r"""Generate api reference docs for `tfmd`.

This requires a local installation of `tfmd` and `tensorflow_docs`

```
$ pip install tensorflow_metadata git+https://github.com/tensorflow/docs
```

```
python build_tfmd_docs.py --output_dir=/tmp/tfmd-api
```

"""
from absl import app
from absl import flags

from tensorflow_docs.api_generator import generate_lib
import tensorflow_metadata as tfmd

# `.proto` (which contains all the classes) is not imported by default
import tensorflow_metadata.proto  # pylint: disable=unused-import

_OUTPUT_DIR = flags.DEFINE_string('output_dir', '/tmp/tfmd_api/',
                                  'The path to output the files to')

_CODDE_URL_PREFIX = flags.DEFINE_string(
    'code_url_prefix',
    'https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto',
    'The url prefix for links to code.')

_SEARCH_HINTS = flags.DEFINE_bool(
    'search_hints', True,
    'Include metadata search hints in the generated files')

_SITE_PATH = flags.DEFINE_string(
    'site_path',
    'tfx/tensorflow_metadata/api_docs/python',
    'Path prefix in the _toc.yaml')


def main(args):
  if args[1:]:
    raise ValueError('Unrecognized Command line args', args[1:])

  doc_generator = generate_lib.DocGenerator(
      root_title='TF-Metadata',
      py_modules=[('tfmd.proto', tfmd.proto)],
      code_url_prefix=_CODDE_URL_PREFIX.value,
      search_hints=_SEARCH_HINTS.value,
      site_path=_SITE_PATH.value,
      callbacks=[])

  doc_generator.build(_OUTPUT_DIR.value)


if __name__ == '__main__':
  app.run(main)
