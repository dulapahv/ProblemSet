#include <stdio.h>

void square_numbers(double *arr, double n) {
    for (int i = 0; i < n; i++)
        arr[i] *= arr[i];
}

int main()
{
    double arr[] = {8, 6.2, 3.1, 4};
    const size_t n = sizeof(arr)/sizeof(arr[0]);
    square_numbers(arr, n);

    for (int i = 0; i < n; i++)
        printf("%f ", arr[i]);
    return 0;
}