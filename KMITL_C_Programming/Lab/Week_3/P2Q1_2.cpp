#include <iostream>

using namespace std;

void print_rect1 (char chr, int width, int height) {
    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {
            cout << chr;
        }
        cout << endl;
    }
}

int main() {
    char usinChr;
    int w, h;
    cin >> usinChr >> w >> h; // example: # 4 6
    print_rect1 (usinChr, w, h);
}