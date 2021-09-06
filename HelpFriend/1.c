#include <stdio.h>

int main()
{
    char ch, file1[50],file2[50],message[50];
    FILE *fs,*ft;
    printf("Enter source file name(with extension): ");
    gets(file1);
    fs = fopen(file1,"r");
    printf("Enter target file name(with extension): ");
    gets(file2);
    ft = fopen(file2,"w");
    for (int ch, b; (ch = fgetc(fs)) != EOF;)
    {
        if(ch == ' ')
        {
            if(b != ' '){
                fputc(ch, ft);
            }
        }
        else
            fputc(ch, ft);
        b = ch;
    }
}

// #include <stdio.h>

// int main()
// {
//     FILE* fs = fopen("in.txt","r");
//     FILE* ft = fopen("out.txt","w");
//     for (int ch, b; (ch = fgetc(fs)) != EOF;) {
//         if(ch == ' ') {
//             if(b != ' ')
//                 fputc(ch, ft);
//         }
//         else
//             fputc(ch, ft);
//         b = ch;
//     }
// }
