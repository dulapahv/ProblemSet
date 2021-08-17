#include <iostream>
#include <string>

using namespace std;

int main() {
    string c;
    getline(cin, c);

    int n = 0;
    for (int i = 0; i < c.size(); i++) {
        if (c[i] == ' ' || c[i] == '\t' || c[i] == '\n')
            n++;
    }
    cout << n << endl;
}