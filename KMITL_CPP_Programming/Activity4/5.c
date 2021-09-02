#include <stdio.h>

#define SIZE 5

int sum_array(const int a[], int n)
{
    int *p, sum = 0;
    for (p = (int *)a; p < a + n; ++p)
        sum += *p;
    return sum;
}

int main() {
    int a[SIZE] = {1, 2, 3, 4, 5};
    printf("Elements in array are: ");
    for (int i = 0; i < SIZE; ++i)
        printf("%d ", a[i]);
    printf("\nSum of array: %d", sum_array(a, SIZE));
}