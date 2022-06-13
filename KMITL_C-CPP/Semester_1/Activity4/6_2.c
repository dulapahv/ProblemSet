#include <stdio.h>

#define SIZE 5

void avg_sum(double a[], int n, double* avg, double* sum)
{
    double* p;
    *sum = 0.0;
    for (p = a; p < a + n; ++p)
        *sum += *p;
    *avg = *sum / n;
}


int main() {
    double a[SIZE] = {1, 2, 3, 4, 5}, avg, sum;
    printf("Elements in array are: ");
    for (int i = 0; i < SIZE; ++i)
        printf("%f ", a[i]);
    avg_sum(a, SIZE, &avg, &sum);
    printf("\nAverage: %f\nSum: %f", avg, sum);
}