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

import os
import platform
import shutil
import subprocess

import setuptools
from setuptools import find_packages
from setuptools import setup
# pylint: disable=g-bad-import-order
# It is recommended to import setuptools prior to importing distutils to avoid
# using legacy behavior from distutils.
# https://setuptools.readthedocs.io/en/latest/history.html#v48-0-0
from distutils.command import build
# pylint: enable=g-bad-import-order


class _BuildCommand(build.build):
  """Build everything that is needed to install.

  This overrides the original distutils "build" command to to run bazel_build
  command before any sub_commands.

  build command is also invoked from bdist_wheel and install command, therefore
  this implementation covers the following commands:
    - pip install . (which invokes bdist_wheel)
    - python setup.py install (which invokes install command)
    - python setup.py bdist_wheel (which invokes bdist_wheel command)
  """

  def _build_cc_extensions(self):
    return True

  # Add "bazel_build" command as the first sub_command of "build". Each
  # sub_command of "build" (e.g. "build_py", "build_ext", etc.) is executed
  # sequentially when running a "build" command, if the second item in the tuple
  # (predicate method) is evaluated to true.
  sub_commands = [
      ('bazel_build', _build_cc_extensions),
  ] + build.build.sub_commands


class _BazelBuildCommand(setuptools.Command):
  """Build Bazel artifacts and move generated files to the ."""

  def initialize_options(self):
    pass

  def finalize_options(self):
    self._bazel_cmd = shutil.which('bazel')
    if not self._bazel_cmd:
      raise RuntimeError(
          'Could not find "bazel" binary. Please visit '
          'https://docs.bazel.build/versions/master/install.html for '
          'installation instruction.')
    if platform.system() == 'Windows':
      self._additional_build_options = ['--copt=-DWIN32_LEAN_AND_MEAN']
    else:
      self._additional_build_options = []

  def run(self):
    subprocess.check_call(
        [self._bazel_cmd, 'run',
         '--compilation_mode', 'opt',
         *self._additional_build_options,
         '//tensorflow_metadata:move_generated_files'],
        # Bazel should be invoked in a directory containing bazel WORKSPACE
        # file, which is the root directory.
        cwd=os.path.dirname(os.path.realpath(__file__)),)


with open('tensorflow_metadata/version.py') as fp:
  globals_dict = {}
  exec(fp.read(), globals_dict)  # pylint: disable=exec-used

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
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    namespace_packages=[],
    install_requires=[
        'absl-py>=0.9,<2.0.0',
        'googleapis-common-protos>=1.52.0,<2',
        'protobuf>=3.20.3,<5',
    ],
    python_requires='>=3.9,<4',
    packages=find_packages(),
    include_package_data=True,
    description='Library and standards for schema and statistics.',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='tensorflow metadata tfx',
    download_url='https://github.com/tensorflow/metadata/tags',
    requires=[],
    cmdclass={
        'build': _BuildCommand,
        'bazel_build': _BazelBuildCommand,
    },
)
