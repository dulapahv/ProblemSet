#include <stdio.h>

int main() {
    int i = 0;

    ++i;
    printf("red, ");
    if (i < 0)
        printf("green");
    else
        printf("blue");
}