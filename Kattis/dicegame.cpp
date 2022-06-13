#include <iostream>

using namespace std;

int main() {
    int usin[2][4];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> usin[i][j];
        }
    }

    int gunnar = 0, emma = 0;
    for (int i = 0; i < 4; i++) {
        gunnar += usin[0][i];
        emma += usin[1][i];
    }

    if (gunnar > emma) {
        cout << "Gunnar" << endl;
    }
    else if (emma > gunnar) {
        cout << "Emma" << endl;
    }
    else {
        cout << "Tie" << endl;  
    }
}