#include <stdio.h>


int main()
{
    int amount3 = 0;
    int amount5 = 0;
    int result3 = 0;

    if (result3 < 10)
    {
        for (int i = 1; i < 10; i++)
        {
            result3 = 3 * i;
            amount3 += 1;
        }
    }
    printf("%i\n", amount3);
}
