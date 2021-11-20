#include <stdio.h>
#include <math.h>

double compute_avg(int *arr, int n) {
    double sum = 0, avg;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    avg = sum / n;
    return avg;
}

double compute_std(int *arr, int n) {
    double avg = compute_avg(arr, n);
    double upper = 0;
    for (int i = 0; i < n; i++)
        upper += pow((arr[i] - avg), 2);
    return sqrt(upper / n);
}

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    printf("%.2f\n", compute_std(arr, n));
}