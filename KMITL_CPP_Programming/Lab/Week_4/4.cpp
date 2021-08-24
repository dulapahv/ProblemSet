#include <iostream>

using namespace std;

int main() {
    FILE* file = fopen("4.txt", "r");
    for (int c; (c = fgetc(file)) != EOF;) {
        if (c == '\\')
            putchar('\\');
        if (c == '\t') {
            putchar('\\');
            putchar('t');
        }
        putchar(c);
    }
    fclose(file);
}