#include <stdio.h>

int main()
{
    int cases;
    scanf("%d", &cases);
    int sol[cases];
    for (int i = 0; i < cases; i++)
    {
        int amount, usin, sum = 0;
        scanf("%d", &amount);
        for (int j = 0; j < amount; j++)
        {
            scanf("%d", &usin);
            sum += usin;
        }
        sol[i] = sum;
    }
    for (int i = 0; i < cases; i++)
    {
        printf("%d\n", sol[i]);
    }
}