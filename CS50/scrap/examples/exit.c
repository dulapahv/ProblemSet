#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("missing command-line argument\n");
        return 1; // Return exit (result) code of 1. Triggered when user doesn't input 2 words
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}

// Running "echo $?" after program is finished will display the exit code