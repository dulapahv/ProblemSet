#include <iostream>

using namespace std;

void print_tri3(char c, int n) {
    for (int i = n; i > 0; i--) {
        for (int j = 1; j < i; j++) {
            cout << " ";
        }
        for (int j = i - 1; j < n; j++) {
            cout << c;
        }
        cout << endl;
    }
}

int main() {
    char usinChar;
    int height;
    cin >> usinChar >> height; // example: * 5
    print_tri3(usinChar, height);
}