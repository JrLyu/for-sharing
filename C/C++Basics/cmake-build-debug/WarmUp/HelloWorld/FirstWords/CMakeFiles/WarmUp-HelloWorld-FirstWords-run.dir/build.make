# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug

# Include any dependencies generated for this target.
include WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/compiler_depend.make

# Include the progress variables for this target.
include WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/progress.make

# Include the compile flags for this target's objects.
include WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/flags.make

WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o: WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/flags.make
WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o: /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/WarmUp/HelloWorld/FirstWords/src/main.cpp
WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o: WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o"
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o -MF CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o.d -o CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o -c /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/WarmUp/HelloWorld/FirstWords/src/main.cpp

WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.i"
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/WarmUp/HelloWorld/FirstWords/src/main.cpp > CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.i

WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.s"
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/WarmUp/HelloWorld/FirstWords/src/main.cpp -o CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.s

# Object files for target WarmUp-HelloWorld-FirstWords-run
WarmUp__HelloWorld__FirstWords__run_OBJECTS = \
"CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o"

# External object files for target WarmUp-HelloWorld-FirstWords-run
WarmUp__HelloWorld__FirstWords__run_EXTERNAL_OBJECTS =

WarmUp/HelloWorld/FirstWords/WarmUp-HelloWorld-FirstWords-run: WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/src/main.cpp.o
WarmUp/HelloWorld/FirstWords/WarmUp-HelloWorld-FirstWords-run: WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/build.make
WarmUp/HelloWorld/FirstWords/WarmUp-HelloWorld-FirstWords-run: WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable WarmUp-HelloWorld-FirstWords-run"
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/build: WarmUp/HelloWorld/FirstWords/WarmUp-HelloWorld-FirstWords-run
.PHONY : WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/build

WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/clean:
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords && $(CMAKE_COMMAND) -P CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/cmake_clean.cmake
.PHONY : WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/clean

WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/depend:
	cd /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/WarmUp/HelloWorld/FirstWords /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords /Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/cmake-build-debug/WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : WarmUp/HelloWorld/FirstWords/CMakeFiles/WarmUp-HelloWorld-FirstWords-run.dir/depend
