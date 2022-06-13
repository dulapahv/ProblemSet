#include <stdio.h>


void swap();


int main() {
   int x = 5;
   int y = 1;
    printf("%d %d\n", x, y);
    swap(&x ,&y);
    printf("%d %d", x, y);
}


void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;

}