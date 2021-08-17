#include <iostream>

using namespace std;

void print_rect2(char sc, char fc, int w, int h) {
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (i == 0 || i == h - 1 || j == 0 || j == w - 1)
                cout << sc;
            else
                cout << fc;            
        }
        cout << endl;
    }
}

int main() {
    char outline, fill;
    int width, height;
    cin >> outline >> fill >> width >> height; // example: = - 6 4
    print_rect2(outline, fill, width, height);
}