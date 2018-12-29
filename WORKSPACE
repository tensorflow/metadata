workspace(name = "tensorflow_metadata")

# Using protobuf version 3.6.0
# We need to import the protobuf library under the name com_google_protobuf
# to enable proto_library support in bazel.
http_archive(
    name = "com_google_protobuf",
    strip_prefix = "protobuf-3.6.0",
    sha256 = "50a5753995b3142627ac55cfd496cebc418a2e575ca0236e29033c67bd5665f4",
    urls = [
        "https://mirror.bazel.build/github.com/google/protobuf/archive/v3.6.0.tar.gz",
        "https://github.com/google/protobuf/archive/v3.6.0.tar.gz",
    ]
)

# required by @com_google_protobuf//:protobuf_python
new_http_archive(
    name = "six_archive",
    build_file = "@com_google_protobuf//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    urls = [
        "https://mirror.bazel.build/pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz",
        "https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz",
    ],
)
bind(
    name = "six",
    actual = "@six_archive//:six",
)
