#include <stdio.h>

int main() {
    FILE* in_file = fopen("2_3in.txt", "rb");
    int count = 0;
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            printf("\n");
            count = 0;
        }
        printf("%d ", c);
        count++;
    }
    fclose(in_file);
    return 0;
}