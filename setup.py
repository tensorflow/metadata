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
"""Package Setup script for tf.Metadata."""

from setuptools import find_packages
from setuptools import setup

with open('tensorflow_metadata/version.py') as fp:
  globals_dict = {}
  exec (fp.read(), globals_dict)  # pylint: disable=exec-used

# tf.Metadata version.
__version__ = globals_dict['__version__']


# Note: In order for the README to be rendered correctly, make sure to have the
# following minimum required versions of the respective packages when building
# and uploading the zip/wheel package to PyPI:
# setuptools >= 38.6.0, wheel >= 0.31.0, twine >= 1.11.0
# Get the long description from the README file.
with open('README.md') as fp:
  _LONG_DESCRIPTION = fp.read()

setup(
    name='tensorflow-metadata',
    version=__version__,
    author='Google Inc.',
    author_email='tensorflow-extended-dev@googlegroups.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    namespace_packages=[],
    install_requires=[
        'absl-py>=0.7,<0.10',
        'googleapis-common-protos',
        'protobuf>=3.7,<4',
    ],
    python_requires='>=3.5,<4',
    packages=find_packages(),
    include_package_data=True,
    description=('Library and standards for schema and statistics.'),
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='tensorflow metadata tfx',
    download_url='https://github.com/tensorflow/metadata/tags',
    requires=[])
