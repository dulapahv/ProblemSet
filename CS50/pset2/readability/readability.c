#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

// Prototype function
// Count letter(s)
int count_letter(string text);
// Count word(s)
int count_word(string text);
// Count sentence(s)
int count_sentence(string text);

int main(void)
{
    // Prompt the user for a string of text
    string text = get_string("Input your text: ");

    // Compute the grade
    int index = round(0.0588 * count_letter(text) - 0.296 * count_sentence(text) - 15.8);;
    // Print out grade
    //printf("%i word(s)\n", count_word(text)); // DEBUG
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

// Begin of custom function
// Count letter(s) per 100 words. If letter between A-Z or a-z in ASCII is found, + 1 letter
int count_letter(string text)
{
    // Keep track of letter
    int letter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            letter += 1;
        }
        else if (text[i] >= 'a' && text[i] <= 'z')
        {
            letter += 1;
        }
    }
    letter = (100 * letter) / count_word(text);
    //printf("%i letter(s)\n", letter); // DEBUG
    return letter;
}

// Count word(s). If ' ' (spaces) are found in text, + (n + 1) word (ex: 1 space = 2 words)
int count_word(string text)
{
    // Keep track of word
    int word = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            word += 1;
        }
    }
    return word;
}

// Count sentence(s). Count number of ?, !, . symbol
int count_sentence(string text)
{
    // Keep track of sentence
    int sentence = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '!' || text[i] == '?' || text[i] == '.')
        {
            sentence += 1;
        }
    }
    sentence = (100 * sentence) / count_word(text);
    //printf("%i sentence(s)\n", sentence); // DEBUG
    return sentence;
}