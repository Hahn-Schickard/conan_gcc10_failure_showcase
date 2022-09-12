# Description

This is a minimal viable project set up to reproduce [[bug] conan create fails to properly set shared library links for built target when using gcc 10](https://github.com/conan-io/conan/issues/10745)

## Requires
1. CMake
2. Conan 
3. gcc (Debian 10.2.1-6) 10.2.1 20210110 (to reproduce the bug on conan 1.46) 

## Conan Profile
```
[settings]
os=Linux
os_build=Linux
arch=x86_64
arch_build=x86_64
compiler=gcc
compiler.version=10
compiler.libcxx=libstdc++11
build_type=Release
[options]
[build_requires]
[env]
```

## Building
1. Call `mkdir build && cd build` to create a build directory
2. Call `cmake -DCMAKE_BUILD_TYPE=Release ..` to generate cmake project configuration
3. Call `cmake --build .` to build the project

## Unit testing

In build directory use `ctest --verbose` to run the unit tests

## Local Test

To run the local test, execute `./build/sources/local_test/GCC10_Failure_Local_Test`, the program should print out `Hello World!` into your console screen

## Packaging
Use `conan create conan 0.1.0@showcase/development` to build the package
