workspace(name = "tensorflow_metadata")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "97e70364e9249702246c0e9444bccdc4b847bed1eb03c5a3ece4f83dfe6abc44",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz",
    ],
)

_PROTOBUF_COMMIT = "90b73ac3f0b10320315c2ca0d03a5a9b095d2f66"  # 3.21.9

http_archive(
    name = "com_google_protobuf",
    sha256 = "f5ba48be0fd7a32daa6900b9bbf90b1cb0af9fc696ee7d71455149898f46ee46",
    strip_prefix = "protobuf-%s" % _PROTOBUF_COMMIT,
    urls = [
        "https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/protobuf/archive/%s.tar.gz" % _PROTOBUF_COMMIT,
        "https://github.com/protocolbuffers/protobuf/archive/%s.tar.gz" % _PROTOBUF_COMMIT,
    ],
)

# Needed by com_google_protobuf.
http_archive(
    name = "zlib",
    build_file = "@com_google_protobuf//:third_party/zlib.BUILD",
    sha256 = "d8688496ea40fb61787500e863cc63c9afcbc524468cedeb478068924eb54932",
    strip_prefix = "zlib-1.2.12",
    urls = ["https://github.com/madler/zlib/archive/v1.2.12.tar.gz"],
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

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
protobuf_deps()

load("@bazel_skylib//lib:versions.bzl", "versions")
versions.check("5.3.0")
