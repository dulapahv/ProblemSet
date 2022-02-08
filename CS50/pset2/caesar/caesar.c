#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// Store value of key globally
int key = 0;

// Prompt user for command-line argument (key)
int main(int argc, string argv[])
{
    // Check whether there's argument or not. "argc == 1" is the program name
    // If there's only the program name (no argument) then exit
    if (argc == 1)
    {
        printf("./caesar key\n");
        return 1;
    }
    // Accessing argv[] without argc > 1 will trigger "Segmentation fault" error
    else
    {
        // Convert the first argument into int.
        key = atoi(argv[1]);

        // Making sure that user only input integer
        if (atoi(argv[1]) == 0)
        {
            printf("./caesar key\n");
            return 1;
        }

        // Because the character will be the same after shifting 26 times,
        // This will get the lowest possible number of shifting
        for (int i = 0; i < key; i++)
        {
            if (i >= 26)
            {
                key -= 26;
            }
        }

        // Prompt user for plain text
        string plaintext = get_string("plaintext: ");

        // Shift text according to number of key
        for (int i = 0, len = strlen(plaintext); i < len; i++)
        {
            if (isupper(plaintext[i]))
            {
                // Make text start again at the first/last position
                plaintext[i] = key - (26 - plaintext[i]);
                if (plaintext[i] < 'A')
                {
                    plaintext[i] += 26;
                }
            }
            if (islower(plaintext[i]))
            {
                plaintext[i] = key - (26 - plaintext[i]);
                if (plaintext[i] < 'a')
                {
                    plaintext[i] += 26;
                }
            }
        }
        // Print out the ciphertext
        printf("Ciphertext: %s\n", plaintext);
        return 0;
    }
}
