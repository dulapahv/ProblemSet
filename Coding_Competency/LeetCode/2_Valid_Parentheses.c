#include <stdbool.h>
#include <stdio.h>

bool isValid(char* s) {
    int flag1 = 0;
    int flag2 = 0;
    int flag3 = 0;
    int expect = 0;
    int i = 0;

    while (s[i]) {
        
        i++;
    }
    return (flag1 == 0 && flag2 == 0 && flag3 == 0);
}

int main() {
    char* s = "{[]}";
    printf("%d", isValid(s));
}