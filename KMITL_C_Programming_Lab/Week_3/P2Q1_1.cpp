#include <iostream>

using namespace std;

int main() {
    int width, height;
    cin >> width >> height;

    int sWidth = floor(width / 2), sHeight = floor(height / 2);
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cout << "*";
        }
        cout << endl;
    }
}