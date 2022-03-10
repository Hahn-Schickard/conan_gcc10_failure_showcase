cmake_minimum_required(VERSION 3.6)

set(THIS Unit_Tests_Runner)

find_package(GTest REQUIRED)

file(GLOB Module1_Tests "${CMAKE_CURRENT_LIST_DIR}/Module1_Tests/*")

add_executable(${THIS})
target_sources(${THIS} PRIVATE 
                       "testRunner.cpp"
                       ${Module1_Tests}
)

target_link_libraries(${THIS} PUBLIC
                              GTest::GTest
                              ${PROJECT_NAME}_Module1
)

add_test(
    NAME ${THIS}
    COMMAND ${THIS}
)

set_target_properties(${THIS} PROPERTIES
                              CXX_STANDARD 17
)