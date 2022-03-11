# Description

This is a minimal viable project set up to reproduce [[bug] conan create fails to properly set shared library links for built target when using gcc 10](https://github.com/conan-io/conan/issues/10745)

## Requires
1. CMake
2. Conan 
3. gcc (Debian 10.2.1-6) 10.2.1 20210110 (to reproduce the bug on conan 1.46) 

## Building
1. Call `mkdir build && cd build` to create a build directory
2. Call `cmake ..` to generate cmake project configuration
3. Call `cmake --build .` to build the project

## Unit testing

In build directory use `ctest --verbose` to run the unit tests

## Packaging
Use `conan create conan 0.1.0@showcase/development` to build the package
