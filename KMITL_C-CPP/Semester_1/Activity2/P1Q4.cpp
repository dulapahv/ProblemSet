#include <iostream>
#include <string>

using namespace std;

int main() {
    int usin;
    cout << "Enter Text: ";

    while ((usin = getchar()) != EOF) {
        if (usin == '\t') {
            putchar('\\');
            putchar('t');
        }
        if (usin == '\\') {
            putchar('\\');
            putchar('\\');
        }
        if (usin != '\t' && usin != '\\') {
            putchar(usin);
        }
    }
}