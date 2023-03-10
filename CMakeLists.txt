cmake_minimum_required(VERSION 3.0.0)
project(qmk_rgb_simulator VERSION 0.1.0)

include(CTest)
enable_testing()

FILE(GLOB BaseSrc src/thor/src/*.c)
FILE(GLOB RgbMatrixSrc src/thor/src/rgb_matrix/*.c)
FILE(GLOB Lib8tion src/thor/src/lib8tion/*.h)

add_executable(qmk_rgb_simulator
    ${BaseSrc}
    ${RgbMatrixSrc}
    ${Lib8tion}
)

target_include_directories (qmk_rgb_simulator PUBLIC src/thor/src)
target_include_directories (qmk_rgb_simulator PUBLIC src/thor/src/rgb_matrix)
target_include_directories (qmk_rgb_simulator PUBLIC src/thor/src/rgb_matrix/animations)
target_include_directories (qmk_rgb_simulator PUBLIC src/thor/src/rgb_matrix/animations/runners)
target_include_directories (qmk_rgb_simulator PUBLIC src/thor/src/lib8tion)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
