#include <iostream>

using namespace std;

int main() {
    int width, height;
    cin >> width >> height; // example: 4 6

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cout << "*";
        }
        cout << endl;
    }
}