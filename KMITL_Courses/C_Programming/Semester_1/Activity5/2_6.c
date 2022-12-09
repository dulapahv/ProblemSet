#include <stdio.h>

int main() {
    FILE* in_file = fopen("2_6in.txt", "rb");
    FILE* out_file = fopen("2_6out.txt", "wb");
    int firstDigit, secondDigit, thirdDigit;
    int count = 0;
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            fputc('\n', out_file);
            count = 0;
        }
        if (c >= 10 && c < 100) {
            firstDigit = (c / 10) + 48;
            secondDigit = (c % 10) + 48;
            fputc(firstDigit, out_file);
            fputc(secondDigit, out_file);
        }
        else if (c >= 100) {
            firstDigit = (c / 100) + 48;
            secondDigit = ((c / 10) % 10) + 48;
            thirdDigit = (c % 10) + 48;
            fputc(firstDigit, out_file);
            fputc(secondDigit, out_file);
            fputc(thirdDigit, out_file);
        }
        fputc(' ', out_file);
        count++;
    }
    fclose(in_file);
    fclose(out_file);
    return 0;
}