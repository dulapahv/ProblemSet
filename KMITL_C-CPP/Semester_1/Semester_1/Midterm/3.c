#include <stdio.h>

int all_even(int a[], size_t n)
{
    for (int i = 0; i < n; ++i)
        if (a[i] % 2 == 0)
            return 1;
        else
            return 0;
}

int main() {
    int arr[5] = {3, 4, 6, 8, 10};
    printf("%d", all_even(arr, 5));
}
