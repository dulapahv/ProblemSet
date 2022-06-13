#include <stdio.h>

double cal_average(double *arr, double n) {
    double sum = 0, avg;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    avg = sum / n;
    return avg;
}

int main()
{
    double arr[] = {8, 6.2, 3.1, 4};
    const size_t n = sizeof(arr)/sizeof(arr[0]);
    double avg = cal_average(arr, n);
    printf("Average = %.4f\n", avg);
    return 0;
}