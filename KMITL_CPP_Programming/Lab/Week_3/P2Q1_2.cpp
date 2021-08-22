#include <iostream>

using namespace std;

void print_rect1 (char c, int w, int h) {
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << c;
        }
        cout << endl;
    }
}

int main() {
    char usinChr;
    int width, height;
    cout << "Character: ";
    cin >> usinChr;
    cout << "Width: ";
    cin >> width;
    cout << "Height: ";
    cin >> height;
    print_rect1 (usinChr, width, height);
}