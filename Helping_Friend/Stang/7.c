#include <stdio.h>

int main()
{
    int i = 255, x = 0;

    int a[i];

    for (int n = 0; n < i; n++, x++)
    {
        scanf("%d", &a[n]);

        if (a[n] == 0)
            break;
    }
    for (int n = x; n > 0; n--)
    {
        if (a[n - 1] > 0)
            printf("%d\n", a[n - 1]);
    }
    return 0;
}