#include <iostream>

using namespace std;

void print_diamond(char c, int n) {
    int height = n;
    bool even = false;

    if (height % 2 == 0) {
        height -= 1;
        even = true;
    }
    int pattern = 1;
    
    for (int i = 0; i < height / 2; i++) {
        for (int j = 0; j < (height - pattern) / 2; j++) {
            cout << ' ';
        }
        for (int j = 0; j < pattern; j++) {
            cout << c;
        }
        for (int j = 0; j < (height - pattern) / 2; j++) {
            cout << ' ';
        }
        pattern += 2;
        cout << endl;
    }
    for (int i = 0; i < height; i++) {
        cout << c;
    }
    cout << endl;
    pattern -= 2;

    for (int i = 0; i < height / 2; i++) {
        for (int j = (height - pattern) / 2; j > 0; j--) {
            cout << ' ';
        }
        for (int j = 0; j < pattern; j++) {
            cout << c;
        }
        for (int j = (height - pattern) / 2; j > 0; j--) {
            cout << ' ';
        }
        pattern -= 2;
        cout << endl;
    }

    if (even) {
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
    print_diamond(usinChar, height);
}