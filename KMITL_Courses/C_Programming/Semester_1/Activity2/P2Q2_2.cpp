#include <iostream>

using namespace std;

int main() {
    int height;
    cout << "Height: ";
    cin >> height;

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < height - i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}