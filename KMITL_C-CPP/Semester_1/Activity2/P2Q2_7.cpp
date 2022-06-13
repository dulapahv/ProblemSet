#include <iostream>

using namespace std;

void print_tri4(char c, int n) {
    for (int i = n; i > 0; i--) {
        for (int j = 0; j < n - i; j++)
            cout << " ";
        for (int j = 0; j < i; j++) {
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
    print_tri4(usinChar, height);
}