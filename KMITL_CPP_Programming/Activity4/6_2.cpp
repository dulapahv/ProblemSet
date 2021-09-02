#include <stdio.h>

void avg_sum(double a[], int n, double* avg, double* sum)
{
    int* p;
    *sum = 0.0;
    for (p = (int*)a; p < (int*)a + n; ++p)
        *sum += *p;
    *avg = *sum / n;
}


int main() {
    const int n = 5;
    double a[n] = {1, 2, 3, 4, 5}, avg, sum;
    avg_sum(a, n, &avg, &sum);
    printf("%f\n%f", avg, sum);
}