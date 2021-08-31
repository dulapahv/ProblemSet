/* Pseudocode */
// Get character from a file
// Convert to lower case
// Print out the converted character

#include <iostream>

using namespace std;

int main() {
    FILE* file = fopen("5.txt", "r");
    for (int c; (c = fgetc(file)) != EOF;) {
        putchar(tolower(c));
    }
    fclose(file);
}