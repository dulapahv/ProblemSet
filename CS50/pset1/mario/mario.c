\#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get input
    int n;
    do
    {
        n = get_int("Please input height: ");
    }
    while (n < 1 || n > 8); // User input condition

    // Generate output
    for (int i = n; i > 0; i--) // Create number of rows
    {
        for (int j = 1; j < i; j++) // Create number of spaces in each row
        {
            printf(" ");
        }
        for (int k = i - 1; k < n; k++) // Create number of # in each row
        {
            printf("#");
        }
        printf("\n");
    }
}