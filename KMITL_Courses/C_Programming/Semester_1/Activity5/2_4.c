#include <stdio.h>

int main() {
    FILE* in_file = fopen("2_4in.txt", "rb");
    FILE* out_file = fopen("2_4out.txt", "wb");
    int firstDigit, secondDigit, thirdDigit;
    int count = 0;
    char hex[] = {'A', 'B', 'C', 'D', 'E', 'F'};
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (count >= 8) {
            fputc('\n', out_file);
            count = 0;
        }
        if (c >= 'A' && c <= 'Z') {
            if (c >= 'A' && c <= 'I') {
                c -= 24;
                firstDigit = (c / 10) + 48;
                secondDigit = (c % 10) + 48;
                fputc(firstDigit, out_file);
                fputc(secondDigit, out_file);
            }
            else if (c >= 'P' && c <= 'Y') {
                c -= 30;
                firstDigit = (c / 10) + 48;
                secondDigit = (c % 10) + 48;
                fputc(firstDigit, out_file);
                fputc(secondDigit, out_file);
            }
            else if ((c >= 'J' && c <= 'O') || c == 'Z') {
                c -= 102;
                firstDigit = c + 48;
                fputc(firstDigit, out_file);
                fputc(hex[((c + 102) % 16) - 10], out_file);
            }
            fputc(' ', out_file);
        }
        else if (c >= 'a' && c <= 'z') {
            if (c >= 'a' && c <= 'i') {
                c -= 36;
                firstDigit = (c / 10) + 48;
                secondDigit = (c % 10) + 48;
                fputc(firstDigit, out_file);
                fputc(secondDigit, out_file);
            }
            else if (c >= 'p' && c <= 'y') {
                c -= 42;
                firstDigit = (c / 10) + 48;
                secondDigit = (c % 10) + 48;
                fputc(firstDigit, out_file);
                fputc(secondDigit, out_file);
            }
            else if ((c >= 'j' && c <= 'o') || c == 'z') {
                c -= 102;
                firstDigit = c + 48;
                fputc(firstDigit, out_file);
                fputc(hex[((c + 102) % 16) - 10], out_file);
            }
            fputc(' ', out_file);
        }
        else if (c == '\n') {
            int arr[6] = {'0', 'D', ' ', '0', 'A', ' '};
            for (int i = 0; i < 6; i++)
                fputc(arr[i], out_file);
        }
        count++;
    }
    fclose(in_file);
    fclose(out_file);
    return 0;
}