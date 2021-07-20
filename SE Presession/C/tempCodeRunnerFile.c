#include <stdio.h>
#include <string.h>

#define size 16

int word[size];

int trial = 10;
char guess;

int main()
{
    int key, index = -1;
    
    scanf("%s", &word);

    for (int i = 0; i < 10; i++)
    {
        if (word != NULL)
        {
            scanf("%c", &guess);

            for (int j = 0; j < size; j++)
            {
                if (word[j] == guess)
                {
                    key = j;
                    break;
                }
            }

            if (index != -1)
            {
                printf("CORRECT");
                for (int k = index; k < size; k++)
                {
                    word[k] == word[k + 1];
                }
            }
            else
            {
                if (trial == 0)
                {
                    printf("LOOSE");
                    break;
                }
                else
                {
                    printf("TRIAL -1");
                    trial -= 1;
                }
            }
        }
        else
        {
            printf("WIN");
            break;
        }
    }
}