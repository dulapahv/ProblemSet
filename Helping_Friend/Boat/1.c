#include <stdio.h>

double compute_avg(int *arr, int n) {
    double sum = 0, avg;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    avg = sum / n;
    return avg;
}

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    printf("%.2f\n", compute_avg(arr, n));
}