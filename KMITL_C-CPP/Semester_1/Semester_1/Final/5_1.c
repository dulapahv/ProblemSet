#include <stdio.h>
#include <stdlib.h>

#define ROW 4
#define COLUMN 4

int main() {
    const double data[] = {
        1.2, 3.1, 2.2, 1.3, 3.4, 1.6,
        2.1, 3.2, 2.4, 1.1, 3.4, 1.4,
        1.7
    };

    int size = sizeof(data) / sizeof(data[0]);
    double **array;
    array = (double **)malloc(sizeof(double*));
    for (int i = 0; i < size; i++)
        array[i] = (double *)malloc(sizeof(double));

    int index = 0;
    for (int i = 0; i < ROW; i++)
        for (int j = 0; j < COLUMN; j++) {
            array[i][j] = data[index];
            index++;
    }

    for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COLUMN; j++)
            printf("%.2lf ", array[i][j]);
        printf("\n");
    }

    for (int i = 0; i < size; i++)
        free(array[i]);
    free(array);
   
    return 0;
}