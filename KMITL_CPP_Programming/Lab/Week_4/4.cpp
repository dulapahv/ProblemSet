/* Pseudocode */
// Get character from a file
// Check if character is backslash. If so, print out another backslash to make it appeared "\\"
// Check if character is a tab. If so, print out "\t"
// If it is neither of them, print out the character itself

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