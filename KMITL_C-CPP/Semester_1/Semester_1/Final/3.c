#include <stdio.h>

int sum_odd(int a[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++)
        if (a[i] % 2 != 0)
            sum += a[i];
    return sum;
}

// int sum_odd(int *a, int n) {
//     int sum = 0;
//     for (int *i = a; *i < n; i++)
//         if (*i % 2 != 0)
//             sum += *i;
//     return sum;
// }

int main() {
    int arr[6] = {1, 2, -3, -4, 5, 6};
    int result = sum_odd(arr, 6);
    printf("%d", result);
}