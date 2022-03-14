from conans import ConanFile, CMake, tools
from conans.tools import load
import re
import os


class PackageConan(ConanFile):
    license = "Apache 2.0"
    topics = ("conan_package_failure", "gcc10_failure_showcase")
    build_requires = "gtest/1.10.0"
    requires = []
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False]}
    default_options = {"shared": True,
                       "fPIC": True}
    default_user = "showcase"
    exports_sources = [
        "../cmake*",
        "../includes*",
        "../sources*",
        "../unit_tests*",
        "../CMakeLists.txt",
        "../conanfile.txt",
    ]
    _cmake = None
    generators = "cmake"

    @property
    def _source_subfolder(self):
        current_file_loc = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(current_file_loc, "..")

    def set_name(self):
        content = load(os.path.join(self._source_subfolder, "CMakeLists.txt"))
        name = re.search("set\(THIS (.*)\)", content).group(1)
        self.name = name.strip()

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.verbose = True
        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = self.name
        self.cpp_info.names["cmake_find_package_multi"] = self.name
        self.cpp_info.libs = tools.collect_libs(self)
        self.output.info("Collected libs: {}".format(
            ", ".join(self.cpp_info.libs)))
