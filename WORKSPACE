workspace(name = "tensorflow_metadata")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    urls = [
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.9.0/bazel-skylib-1.9.0.tar.gz",
    ],
)

_PROTOBUF_VERSION = "6.31.1"

http_archive(
    name = "com_google_protobuf",
    sha256 = "6e09bbc950ba60c3a7b30280210cd285af8d7d8ed5e0a6ed101c72aff22e8d88",
    strip_prefix = "protobuf-%s" % _PROTOBUF_VERSION,
    urls = [
        "https://github.com/protocolbuffers/protobuf/archive/refs/tags/v%s.zip" % _PROTOBUF_VERSION,
    ],
)

# Needed by com_google_protobuf.
http_archive(
    name = "zlib",
    build_file = "@com_google_protobuf//:third_party/zlib.BUILD",
    sha256 = "17e88863f3600672ab49182f217281b6fc4d3c762bde361935e436a95214d05c",
    strip_prefix = "zlib-1.3.1",
    urls = ["https://github.com/madler/zlib/archive/v1.3.1.tar.gz"],
)

# Needed by com_google_protobuf.
http_archive(
    name = "six_archive",
    build_file = "@com_google_protobuf//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    urls = ["https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55"],
)

# Needed by com_google_protobuf.
bind(
    name = "six",
    actual = "@six_archive//:six",
)

http_archive(
    name = "rules_python",
    urls = ["https://github.com/bazelbuild/rules_python/archive/refs/tags/0.31.0.tar.gz"],
    strip_prefix = "rules_python-0.31.0",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

local_repository(
    name = "compatibility_proxy",
    path = "third_party/dummy_compatibility_proxy",
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
protobuf_deps()

load("@bazel_skylib//lib:versions.bzl", "versions")
versions.check("7.4.1")
