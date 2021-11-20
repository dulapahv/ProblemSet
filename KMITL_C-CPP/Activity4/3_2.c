#include <stdio.h>

#define HEIGHT 3
#define WIDTH 5

int main() {
    int number[HEIGHT][WIDTH];
    for (int i = 0; i < HEIGHT; i++)
        for (int j = 0; j < WIDTH; j++)
            scanf("%d", &number[i][j]);

    printf("Row totals: ");
    for (int i = 0; i < HEIGHT; i++) {
        int row = 0;
        for (int j = 0; j < WIDTH; j++)
            row += number[i][j];
        printf("%d ", row);
    }

    printf("\nColumn totals: ");
    for (int i = 0; i < WIDTH; i++) {
        int column = 0;
        for (int j = 0; j < HEIGHT; j++)
            column += number[j][i];
        printf("%d ", column);
    }
}