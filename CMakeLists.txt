cmake_minimum_required(VERSION 3.6)

set(THIS GCC10_Failure)

project(${THIS} CXX) 

set(INCLUDES_DIR "${PROJECT_SOURCE_DIR}/includes")
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(GNUInstallDirs)
include(macros)

option(USE_CONAN "Enables integeated conan package manager module. (Requires conan and python3 to be installed)" ON)
if(USE_CONAN)
        if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
        file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.16.1/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake"
                EXPECTED_HASH SHA256=396e16d0f5eabdc6a14afddbcfff62a54a7ee75c6da23f32f7a31bc85db23484
                TLS_VERIFY ON
        )
        endif()

        include(${CMAKE_BINARY_DIR}/conan.cmake)
        list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
        list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

        if(CONAN_EXPORTED)
                include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
                conan_basic_setup()
        else()                
                conan_cmake_autodetect(settings 
                                       BUILD_TYPE ${TYPE} 
                )
                conan_cmake_install(PATH_OR_REFERENCE ${PROJECT_SOURCE_DIR} 
                                    BASIC_SETUP CMAKE_TARGETS
                                    BUILD missing
                                    SETTINGS ${settings}
                )
        endif()
endif()


add_subdirectory(sources)

option(RUN_TESTS "Enables Unit tests runner (Requires GTest framework)" ON)
if(RUN_TESTS)
        enable_testing()
        add_subdirectory(unit_tests)
endif()

if(EXISTS ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in)
        message(STATUS "Pacakge input file: ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in already exists, removing it!")
        file(REMOVE ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in)
endif()

message(STATUS "Creating package input file: ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in")
file(WRITE ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in "@PACKAGE_INIT@ \ninclude(\"\${CMAKE_CURRENT_LIST_DIR}/@PROJECT_NAME@Targets.cmake\")")
file(APPEND ${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in "\ncheck_required_components(\"@PROJECT_NAME@\")")

include(CMakePackageConfigHelpers)	

configure_package_config_file(		
  "${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in"		
  "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"		
  INSTALL_DESTINATION ${THIS_PACKAGE_NAME}/
)	

install(EXPORT ${PROJECT_NAME}Targets		
        FILE ${PROJECT_NAME}Targets.cmake		
        NAMESPACE ${PROJECT_NAME}::		
        DESTINATION ${CMAKE_INSTALL_PREFIX}
)

install(FILES 
        ${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
        DESTINATION ${CMAKE_INSTALL_PREFIX}
)
