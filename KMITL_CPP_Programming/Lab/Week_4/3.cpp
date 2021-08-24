#include <iostream>

using namespace std;

int main() {
    FILE* file = fopen("3.txt", "r");
    for (int c, cEnd; (c = fgetc(file)) != EOF;) {
        if (c == ' ') {
            if (cEnd != ' ')
            putchar(c);
        }
        else
            putchar(c);
        cEnd = c;
    }
}