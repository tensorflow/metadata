workspace(name = "tensorflow_metadata")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

git_repository(
    name = "protobuf_bzl",
    # v3.4.0
    commit = "80a37e0782d2d702d52234b62dd4b9ec74fd2c95",
    remote = "https://github.com/google/protobuf.git",
)
bind(
    name = "protobuf",
    actual = "@protobuf_bzl//:protobuf",
)
bind(
    name = "protobuf_python",
    actual = "@protobuf_bzl//:protobuf_python",
)
bind(
    name = "protobuf_python_genproto",
    actual = "@protobuf_bzl//:protobuf_python_genproto",
)
bind(
    name = "protoc",
    actual = "@protobuf_bzl//:protoc",
)
# Using protobuf version 3.6.0
http_archive(
    name = "protobuf_archive",
    strip_prefix = "protobuf-3.6.0",
    urls = ["https://github.com/google/protobuf/archive/v3.6.0.zip"],
)

# required by protobuf_python
http_archive(
    name = "six_archive",
    build_file = "@protobuf_bzl//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    url = "https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55",
)
bind(
    name = "six",
    actual = "@six_archive//:six",
)
