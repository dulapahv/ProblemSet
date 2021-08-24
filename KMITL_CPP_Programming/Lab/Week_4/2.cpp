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