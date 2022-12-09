#include <stdio.h>

#define HEIGHT 3
#define WIDTH 5

int main() {
    int number[HEIGHT][WIDTH];
    for (int i = 0; i < HEIGHT; i++)
        for (int j = 0; j < WIDTH; j++)
            scanf("%d", &number[i][j]);

    int result[HEIGHT * WIDTH], x = 0;
    for (int i = 0; i < HEIGHT; i++)
        for (int j = 0; j < WIDTH; j++) {
            result[x] = number[i][j];
            x++;
        }

    printf("\nElements in one-dimensional array are:\n");
    for (int i = 0; i < HEIGHT * WIDTH; i++)
        printf("%d ", result[i]);

    printf("\n\nRow totals: ");
    int a = 0;
    for (int i = 0; i < HEIGHT; i++) {
        int row = 0;
        for (int j = 0; j < WIDTH; j++) {
            row += result[a];
            a++;
        }
        printf("%d ", row);
    }

    printf("\nColumn totals: ");
    for (int i = 0; i < WIDTH; i++) {
        int column = 0, b = 0;
        for (int j = 0; j < HEIGHT; j++) {
            column += result[b + i];
            b += 5;
        }
        printf("%d ", column);
    }
}