#include <iostream>
#include <string>

using namespace std;

int main() {
    string c;
    cout << "Enter Text: ";
    getline(cin, c);
    cout << endl;

    int blanks = 0, tabs = 0, newlines = 0;
    for (int i = 0; i < c.size(); i++) {
        if (c[i] == ' ')
            blanks++;
        else if (c[i] == '\t')
            tabs++;
        else if (c[i] == '\n')
            newlines++;
    }
    cout << "Blanks: " << blanks << endl;
    cout << "Tabs: " << tabs << endl;
    cout << "Newlines: " << newlines << endl;
}