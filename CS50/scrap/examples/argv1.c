#include <cs50.h>
#include <stdio.h>

// Take command-line argument input. Doesn't have to be precisely argc and so forth
// "int argc (argument count)" takes in integer, and "string argv[] (argument vector)" takes in an array of strings
int main(int argc, string argv[])
{
    if (argc == 2) // If user input 2 words, including program's name. For ex: ./argv Bryan = 2 words
    {
        printf("hello, %s\n", argv[1]); // argv[0] will print out the program's name
    }
    else
    {
        printf("hello, world\n"); // If user doesn't input 2 words, print out this string
    }
}

// If user input two arguments (including a program's name), print out hello, [name]
// For example: ./argv Bryan -> hello, Bryan
// If user doesn't input any argument, print out "hello, world\n"