cmake_minimum_required(VERSION 3.6) 

set(THIS Module2)
set(MODULE_NAME ${PROJECT_NAME}_${THIS})

list(APPEND THIS_INCLUDES_DIRS
            ${INCLUDES_DIR}/module2
)
INCLUDE_DIRS_AND_FILES("${THIS_INCLUDES_DIRS}" THIS_INCLUDES)

file(GLOB sources "${CMAKE_CURRENT_LIST_DIR}/*.cpp")

add_library(${MODULE_NAME})                

target_sources(${MODULE_NAME} PRIVATE 
                       ${THIS_INCLUDES}
                       ${sources}
)

target_link_libraries(${MODULE_NAME} PUBLIC
                              ${PROJECT_NAME}_Module1
)

target_include_directories(${MODULE_NAME} INTERFACE
                           $<BUILD_INTERFACE:${INCLUDES_DIR}/module2>
                           $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
                           $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}>
)

target_compile_features(${MODULE_NAME} PUBLIC cxx_std_17)

install(
    TARGETS ${MODULE_NAME}
    EXPORT ${PROJECT_NAME}Targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(
    FILES ${THIS_INCLUDES}
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}
)
