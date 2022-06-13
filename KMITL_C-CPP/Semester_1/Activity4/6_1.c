#include <stdio.h>

#define SIZE 5

void avg_sum(double a[], int n, double* avg, double* sum)
{
    *sum = 0.0;
    for (int i = 0; i < n; ++i)
        *sum += a[i];
    *avg = *sum / n;
}


int main() {
    double a[SIZE] = {1, 2, 3, 4, 5}, avg, sum;
    printf("Elements in array are: ");
    for (int i = 0; i < SIZE; ++i)
        printf("%f ", a[i]);
    avg_sum(a, SIZE, &avg, &sum);
    printf("\nAverage: %f\nSum of array: %f", avg, sum);
}