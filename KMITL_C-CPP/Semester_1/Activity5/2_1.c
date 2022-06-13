#include <stdio.h>

int main() {
    FILE* in_file = fopen("2_1in.txt", "rb");
    int count = 0;
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            printf("\n");
            count = 0;
        }
        printf("%02X ", c);
        count++;
    }
    fclose(in_file);
    return 0;
}