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
    avg_sum(a, SIZE, &avg, &sum);
    printf("Average: %f\nSum of array: %f", avg, sum);
}