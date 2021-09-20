#include <stdio.h>

int main() {
    int n, val;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    scanf("%d", &val);
    for (int i = 0; i < n; i++)
        if (val == arr[i]) {
            printf("%d", i);
            return 0;
        }
    printf("Not found");
}