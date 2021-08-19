#include <iostream>

using namespace std;

void print(int w, int h, int c) {
    w /= c;
    h /= c;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if ((i + j) % 2 == 0) {
                for (int k = 0; k < c; k++) {
                    for (int l = 0; l < c; l++) {
                        cout << "#";
                    }
                }
                
            }
            else {
                for (int k = 0; k < c; k++) {
                    for (int l = 0; l < c; l++) {
                        cout << "$";
                    }
                }
                
            }
        }
        cout << endl;
    }
}

int main() {
    int width, height, checker;
    cin >> width >> height >> checker;
    print(width, height, checker);
}
