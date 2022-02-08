#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start;
    do
    {
        start = get_int("Positive Integer: "); // Get start
    }
    while (start < 9);
    // Prompt for end size
    int end;
    do
    {
        end = get_int("Positive Integer: "); // Get end
    }
    while (end < start);
    // Calculate number of years until we reach threshold
    int years = 0;
    if (start != end) // If start equals to end, years = 0
    {
        do
        {
            start = start + ((start / 3) - (start / 4)); // Calculate new population
            years = years + 1; // +1 year to every calculation done
        }
        while (start < end); // Do the calculation until start is <= end
    }
    else 
    {
        years = 0;
    }
    // Print number of years
    printf("Years: %i\n", years);
}