# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-src"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-build"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/tmp"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/src/googletest-stamp"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/src"
  "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/src/googletest-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/src/googletest-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/Users/richardlyu/Documents/GitHub/Enrichment/C/C++Basics/test-framework/googletest-prefix/src/googletest-stamp${cfgdir}") # cfgdir has leading slash
endif()
