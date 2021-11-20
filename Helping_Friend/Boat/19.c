#include <stdio.h>

int main() {
    int n, ans = 0;
    scanf("%d", &n);
    int a[n], b[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (int i = 0; i < n; i++)
        scanf("%d", &b[i]);
    for (int i = 0; i < n; i++)
        ans += a[i] * b[i];
    printf("%d\n", ans);
}