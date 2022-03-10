cmake_minimum_required(VERSION 3.6)

set(THIS GCC10_Failure)

project(${THIS} CXX) 

enable_testing()

set(INCLUDES_DIR "${PROJECT_SOURCE_DIR}/includes")
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(GNUInstallDirs)
include(conan_install)
include(macros)

option(USE_CONAN "Enables integeated conan package manager module. (Requires conan and python3 to be installed)" ON)

if(USE_CONAN)
        include(conan_install)
        execute_conan_install()
endif()


add_subdirectory(sources)
add_subdirectory(unit_tests)

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
