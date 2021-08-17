#include <iostream>

using namespace std;

void print(int w, int h) {
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if ((i + j) % 2 == 0)
                cout << "#";
            else
                cout << "-";
        }
        cout << endl;
    }
}

int main() {
    int width, height;
    cin >> width >> height;
    print(width, height);
}