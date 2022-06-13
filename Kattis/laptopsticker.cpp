#include <iostream>

using namespace std;

int main() {
    int usin[4];
    for (int i = 0; i < 4; i++) {
        cin >> usin[i];
    }

    if (usin[0] - usin[2] < 2) {
        cout << "0" << endl;
    }    
    else if (usin[1] - usin[3] < 2) {
        cout << "0" << endl;
    }
    else {
        cout << "1" << endl;
    }
}