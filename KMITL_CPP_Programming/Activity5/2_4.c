#include <stdio.h>

int main() {
    FILE* in_file = fopen("2_4in.txt", "rb");
    FILE* out_file = fopen("2_4out.txt", "wb");
    int count = 0;
    char hex[16] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'};
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            printf("\n");
            count = 0;
        }
        int temp = 0;
        if (c >= 'A' && c <= 'Z') {
            temp = (c % 16) + 40;

        }
        else if (c >= 'a' && c <= 'z')
            temp = (c % 16) + 60;
        else
            temp = c % 16;
        printf("%d\n", temp);

        fputc(c, out_file);
        count++;
    }
    fclose(in_file);
    fclose(out_file);
    return 0;
}
