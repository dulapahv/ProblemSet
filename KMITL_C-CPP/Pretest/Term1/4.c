#include <stdio.h>

const char text[] = "xyz[20] = { 1, 2, 3 }";

int main() {
    int count = 0;
    for (int i = 0; i < sizeof(text)/sizeof(text[0]); i++) {
        if (text[i] == '=' || text[i] == ',')
            count++;
    }
    printf("Occurrences: %d\n", count);
    return 0;
}