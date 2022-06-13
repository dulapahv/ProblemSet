#include <stdio.h>

// int func1(char c)
// {
//     int n = 0;
//     int i = 0;
//     if (++i && c == '[') {
//         ++n;
//         printf("HI\n");
//     }
//     if (++i && c == ']') {
//         ++n;
//         printf("HI\n");
//     }
//     return i + n;
// }

int func2(char c)
{
    int n = 0;
    int i = 0;
    if (++i && c == '[') {
        ++n;
        printf("HI\n");
    }
    else if (++i && c == ']') {
        ++n;
        printf("HI\n");
    }
    return i + n;
}

int main() {
    int val = func2('+') ;
    printf("%d", val);
}