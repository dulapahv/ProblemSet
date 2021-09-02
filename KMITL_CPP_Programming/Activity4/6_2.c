#include <stdio.h>

#define SIZE 5

void avg_sum(double a[], int n, double* avg, double* sum)
{
    int* p;
    *sum = 0.0;
    for (p = (int*)a; p < (int*)a + n; ++p)
        *sum += *p;
    *avg = *sum / n;
}


int main() {
    double a[SIZE] = {1, 2, 3, 4, 5}, avg, sum;
    avg_sum(a, SIZE, &avg, &sum);
    printf("%f\n%f", avg, sum);
}