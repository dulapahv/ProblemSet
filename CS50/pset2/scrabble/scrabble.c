#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10}; // A = 1, B = 3,...,Z = 10

// Prototype function called "compute_score". The () specify the type of input as well as name of the input variable
int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words. Gets value from "return score;" from the compute_score function
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word) // Start of the custom function that compute the score
{
    // Keep track of score
    int score = 0;

    // Compute and return score for string
    // Continue looping as long as var. "i" is lower than var. "len"
    // (Given that var. "len" = strlen(string length) of the input var. "word")
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            // word[i] will get the value of each character in the input word (i increases with every loop).
            // Then subtract with the value of ASCII of 'A', 65 (For ex: char. 'B' - 'A' = 1).
            // POINTS[] will reference the value inside to the "int POINTS[]" above.
            // +- For ex: Z = Z + X or Z += X
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score; // Output (result) of the function
}
