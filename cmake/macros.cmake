# Internal Helper Functions
# @Author: Dovydas Girdvainis
# @Date: 2020-02-12

# Adds a given directories to those the compiler uses to search for include files.
FUNCTION(INCLUDE_DIRS directory_list)
    foreach(directory ${directory_list})
        include_directories(${directory})
    endforeach()
ENDFUNCTION()

# Expands global include file list and appeds each directory and sub-directory to those the compiler uses to search for include files.
FUNCTION(INCLUDE_DIRS_AND_FILES directory_list included_file_list)
    INCLUDE_DIRS("${directory_list}")
    foreach(directory ${directory_list})
        file(GLOB tmp_file_list ${directory}/*.hpp)
        list(APPEND included_file_list ${tmp_file_list})
    endforeach()
    set(${included_file_list} ${${included_file_list}} PARENT_SCOPE)
ENDFUNCTION()
