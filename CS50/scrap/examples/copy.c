#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h> //Include <stdlib.h> everytime to use malloc
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    strcpy(t, s);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    //Free variable everytime when you use malloc on that variable
    //Use Valgrind to check for memory leak
    free(t);
}