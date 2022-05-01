cmake_minimum_required(VERSION 3.0.0)
project(lab8 VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(lab8 main.cpp Point.cpp Point3D.cpp Point4D.cpp PointND.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
