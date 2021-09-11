#include <stdio.h>
int main()
{
    //Ascii value of 1
    int ch = 50;
    FILE *fp = NULL;
    //Open file in append mode
    fp = fopen("out.txt", "a");
    if(fp == NULL)
    {
        printf("Error in creating the file\n");
        exit(1);
    }
    //Write 1 in file
    fputc(ch, fp);
    //close the file
    fclose(fp);
    printf("Append 1 to the created file\n");
    return 0;
}