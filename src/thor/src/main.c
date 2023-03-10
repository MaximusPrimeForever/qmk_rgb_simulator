#include <stdio.h>

#include "rgb_matrix.h"
#include "config.h"


void main(){
    printf("Hello world\n");
    printf("Calling rgb_task_render:\n");
    rgb_task_render(0);
}

void run_matrix_loop() {
    while (true) {
        rgb_matrix_task();
    }
}