#include <iostream>

using namespace std;

int main() {
    int usin[6];
    for (int i = 0; i < 6; i++) {
        cin >> usin[i];
    }

    if (usin[0] != 1) {
        usin[0] = 1 - usin[0];
    }
    else {
        usin[0] = 0;
    }

    if (usin[1] != 1) {
        usin[1] = 1 - usin[1];
    }
    else {
        usin[1] = 0;
    }

    if (usin[2] != 2) {
        usin[2] = 2 - usin[2];
    }
    else {
        usin[2] = 0;
    }

    if (usin[3] != 2) {
        usin[3] = 2 - usin[3];
    }
    else {
        usin[3] = 0;
    }

    if (usin[4] != 2) {
        usin[4] = 2 - usin[4];
    }
    else {
        usin[4] = 0;
    }

    if (usin[5] != 8) {
        usin[5] = 8 - usin[5];
    }
    else {
        usin[5] = 0;
    }

    for (int i = 0; i < 6; i++) {
        cout << usin[i] << " ";
    }
}