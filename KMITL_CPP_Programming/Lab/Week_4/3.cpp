/* Pseudocode */
// Get character from a file
// Check if character is blank. If so, check whether previous character is not blank. If so, print out the character itself
// But if the character is not blank, print out the character itself
// Store the previous character in the variable to be checked next time

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