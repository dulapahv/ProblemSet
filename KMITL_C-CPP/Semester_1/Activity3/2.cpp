/* Pseudocode */
// Get character from a file
// Check if character is blanks, tabs, or newlines. If so, count them in each category
// Print out the number of counted blanks, tabs, and newlines

#include <iostream>

using namespace std;

int main() {
    int blanks = 0, tabs = 0, newlines = 0;
    FILE* file = fopen("2.txt", "r");
    for (int c; (c = fgetc(file)) != EOF;) {
        if (c == ' ')
            blanks++;
        if (c == '\t')
            tabs++;
        if (c == '\n')
            newlines++;
    }

    cout << "Blanks: " << blanks << endl;
    cout << "Tabs: " << tabs << endl;
    cout << "Newlines: " << newlines << endl;
    fclose(file);
}