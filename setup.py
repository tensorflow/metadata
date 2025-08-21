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

import pathlib
import platform
import shutil
import subprocess

from setuptools import find_packages, setup
from setuptools.command import build_py


class _BazelBuildCommand(build_py.build_py):
    """Build Bazel artifacts and move generated files to the source directory."""

    def initialize_options(self):
        super().initialize_options()
        self._bazel_cmd = shutil.which("bazel")
        if not self._bazel_cmd:
            raise RuntimeError(
                'Could not find "bazel" binary. Please visit '
                "https://docs.bazel.build/versions/master/install.html for "
                "installation instruction."
            )

        self._additional_build_options = []
        if platform.system() == "Windows":
            self._additional_build_options = ["--copt=-DWIN32_LEAN_AND_MEAN"]

    def run(self):
        subprocess.check_call(
            [
                self._bazel_cmd,
                "run",
                "--compilation_mode",
                "opt",
                *self._additional_build_options,
                "//tensorflow_metadata:move_generated_files",
            ],
            # Bazel should be invoked in a directory containing bazel WORKSPACE
            # file, which is the root directory.
            cwd=str(pathlib.Path(__file__).parent),
        )

        super().run()


with open("tensorflow_metadata/version.py") as fp:
    globals_dict = {}
    exec(fp.read(), globals_dict)  # pylint: disable=exec-used

# tf.Metadata version.
__version__ = globals_dict["__version__"]


# Note: In order for the README to be rendered correctly, make sure to have the
# following minimum required versions of the respective packages when building
# and uploading the zip/wheel package to PyPI:
# setuptools >= 38.6.0, wheel >= 0.31.0, twine >= 1.11.0
# Get the long description from the README file.
with open("README.md") as fp:
    _LONG_DESCRIPTION = fp.read()

setup(
    name="tensorflow-metadata",
    version=__version__,
    author="Google Inc.",
    author_email="tensorflow-extended-dev@googlegroups.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    namespace_packages=[],
    install_requires=[
        "absl-py>=0.9,<3.0.0",
        'googleapis-common-protos>=1.56.4,<2;python_version>="3.11"',
        'protobuf>=4.25.2;python_version>="3.11"',
        'protobuf>=4.21.6,<4.22;python_version<"3.11"',
    ],
    python_requires=">=3.9,<4",
    packages=find_packages(),
    extras_require={
        "dev": ["precommit"],
        "test": [
            "pytest>=8,<9",
        ],
    },
    description="Library and standards for schema and statistics.",
    long_description=_LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="tensorflow metadata tfx",
    download_url="https://github.com/tensorflow/metadata/tags",
    requires=[],
    cmdclass={"build_py": _BazelBuildCommand},
    package_data={"tensorflow_metadata.proto.v0": ["*.proto"]},
)
