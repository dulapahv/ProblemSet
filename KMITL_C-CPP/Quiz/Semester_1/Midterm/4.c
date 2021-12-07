#include <stdio.h>

void divisible_by_two(int *a, size_t n) {
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0)
            a[i] = -2;
}

int main()
{
    int arr[] = {11, 12, 0, 7, 9, 1, 3, 2};
    const size_t n = sizeof(arr) / sizeof(*arr);
    printf("before: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\nafter: ");
    divisible_by_two(arr, n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}