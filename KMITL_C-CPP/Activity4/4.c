#include <stdio.h>

#define SIZE 10

void fill_zeros(int a[], int n) 
{
    int *p;
    for (p = a; p < a + n; ++p)
        *p = 0;
}

int main() {
    int a[SIZE];
    fill_zeros(a, SIZE);
    printf("Elements in the array are: ");
    for (int i = 0; i < SIZE; i++) {
        printf("%d", a[i]);
    }
}