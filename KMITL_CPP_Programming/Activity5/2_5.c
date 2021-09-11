#include <stdio.h>

void separate_digit(int c, int* first, int* second, int* third) {
    *first = (c / 100);
    *second = ((c / 10) % 10);
    *third = (c % 10);
}

int main() {
    FILE* in_file = fopen("2_5in.txt", "rb");
    FILE* out_file = fopen("2_5out.txt", "wb");
    int firstDigit, secondDigit, thirdDigit;
    int count = 0;
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            fputc('\n', out_file);
            count = 0;
        }
        if (c >= 'A' && c <= 'Z') {
            if (c >= 'A' && c <= 'G')
                c += 36;
            else if (c >= 'H' && c <= 'O')
                c += 38;
            else if (c >= 'P' && c <= 'W')
                c += 40;
            separate_digit(c, &firstDigit, &secondDigit, &thirdDigit);
            fputc('0', out_file);
            fputc(firstDigit + 48, out_file);
            fputc(secondDigit + 48, out_file);
            fputc(thirdDigit + 48, out_file);
            fputc(' ', out_file);
        }
        else if (c >= 'a' && c <= 'z') {
            if (c >= 'a' && c <= 'g')
                c += 44;
            else if (c >= 'h' && c <= 'o')
                c += 46;
            else if (c >= 'p' && c <= 'w')
                c += 48;
            separate_digit(c, &firstDigit, &secondDigit, &thirdDigit);
            fputc('0', out_file);
            fputc(firstDigit + 48, out_file);
            fputc(secondDigit + 48, out_file);
            fputc(thirdDigit + 48, out_file);
            fputc(' ', out_file);
        }
        else if (c == '\n') {
            int arr[10] = {'0', '0', '1', '5', ' ' , '0', '0', '1', '2', ' '};
            for (int i = 0; i < 10; i++)
                fputc(arr[i], out_file);
        }
        count++;
    }
    fclose(in_file);
    fclose(out_file);
    return 0;
}
