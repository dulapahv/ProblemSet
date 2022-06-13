#include <iostream>

using namespace std;

int main() {
    int height;
    cout << "Height: ";
    cin >> height;

    for (int i = height; i > 0; i--) {
        for (int j = 1; j < i; j++) {
            cout << " ";
        }
        for (int j = i - 1; j < height; j++) {
            cout << "*";
        }
        cout << endl;
    }
}