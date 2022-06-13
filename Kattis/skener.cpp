#include <iostream>

using namespace std;

int main() {
    int r, c, zr, zc;
    cin >> r >> c >> zr >> zc;

    char usin[r][c];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> usin[i][j];
        }
    }

    char result[r * zr][c * zc];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[i][j];
        }
    }

    // for (int i = 0; i < r; i++) {
    //     for (int j = 0; j < c; j++) {
    //         cout << usin[i][j];
    //     }
    //     cout << endl;
    // }
}