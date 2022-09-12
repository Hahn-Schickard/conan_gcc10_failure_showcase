cmake_minimum_required(VERSION 3.6) 

set(THIS Local_Test)
set(MODULE_NAME ${PROJECT_NAME}_${THIS})

file(GLOB sources_list "${CMAKE_CURRENT_LIST_DIR}/*.?pp")

add_executable(${MODULE_NAME})

target_sources(${MODULE_NAME} PRIVATE 
                       ${sources_list}
)

target_link_libraries(${MODULE_NAME} PRIVATE
                              ${PROJECT_NAME}_Module2                            
)

target_compile_features(${MODULE_NAME} PUBLIC cxx_std_17)
