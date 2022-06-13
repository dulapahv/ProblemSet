#include <iostream>

using namespace std;

void print_tri1(char c, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            cout << c;
        }
        cout << endl;
    }
}

int main() {
    char usinChar;
    int height;
    cout << "Character: ";
    cin >> usinChar;
    cout << "Height: ";
    cin >> height;
    print_tri1(usinChar, height);
}