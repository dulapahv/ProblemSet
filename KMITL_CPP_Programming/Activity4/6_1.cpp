#include <stdio.h>

void avg_sum(double a[], int n, double* avg, double* sum)
{
    *sum = 0.0;
    for (int i = 0; i < n; ++i)
        *sum += a[i];
    *avg = *sum / n;
}


int main() {
    const int n = 5;
    double a[n] = {1, 2, 3, 4, 5}, avg, sum;
    avg_sum(a, n, &avg, &sum);
    printf("%f\n%f", avg, sum);
}