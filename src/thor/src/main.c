#include <stdio.h>

/* key matrix size */
#define MATRIX_ROWS 6
#define MATRIX_COLS 15

#define DRIVER_1_LED_TOTAL 45
#define DRIVER_2_LED_TOTAL 37
#define RGB_MATRIX_LED_COUNT (DRIVER_1_LED_TOTAL + DRIVER_2_LED_TOTAL)

#include "rgb_matrix.h"
#include "config.h"


void main(){
    printf("Hello world\n");
    printf("Calling rgb_task_render:\n");
    rgb_task_render(0);
}