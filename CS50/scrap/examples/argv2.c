#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Take command-line argument input. Doesn't have to be precisely argc and so forth
// "int argc (argument count)" takes in integer, and "string argv[] (argument vector)" takes in an array of strings
int main(int argc, string argv[])
{
    if (argc == 2) // If user input 2 words, including program's name. For ex: ./argv Bryan = 2 words
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            printf("%c\n", argv[1][i]);
        }
    }
}