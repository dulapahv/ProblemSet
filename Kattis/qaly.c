#include <stdio.h>

int main()
{
    int x, y[200], result = 0;
    scanf("%d", &x);
    for (int i = 0; i < x; i++)
    {
        scanf("%d", &y);
        result += y[0] * y[1];
    }
    printf("%.3lf", result);
}