#include <stdio.h>

void fill_zeros(int a[], int n) 
{
    int *p;
    for (p = a; p < a + n; ++p)
        *p = 0;
}

int main() {
    const int n = 10;
    int a[n];
    fill_zeros(a, n);
    for (int i = 0; i < n; i++) {
        printf("%d", a[i]);
    }
}