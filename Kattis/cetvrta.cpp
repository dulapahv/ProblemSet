#include <iostream>

using namespace std;

int main() {
    int usin[3][2];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    int x;
    if (usin[0][0] == usin[1][0]) {
        x = usin[2][0];
    }
    else if (usin[1][0] == usin[2][0]){
        x = usin[0][0];
    }
    else {
        x = usin[1][0];
    }

    int y;
    if (usin[0][1] == usin[1][1]) {
        y = usin[2][1];
    }
    else if (usin[1][1] == usin[2][1]) {
        y = usin[0][1];
    }
    else {
        y = usin[1][1];
    }

    cout << x << " " << y << endl;
}