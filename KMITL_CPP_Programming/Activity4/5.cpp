#include <stdio.h>

int sum_array(const int a[], int n)
{
    int *p, sum = 0;
    for (p = (int *)a; p < a + n; ++p)
        sum += *p;
    return sum;
}

int main() {
    const int n = 5;
    int a[n] = {1, 2, 3, 4, 5};
    printf("%d", sum_array(a, n));
}