#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int rec[cases][3];
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> rec[i][j];
        }
    }

    for (int i = 0; i < cases; i++) {
        if ((rec[i][1] - rec[i][2]) < rec[i][0]) {
            cout << "do not advertise" << endl;
        }
        else if ((rec[i][1] - rec[i][2]) > rec[i][0])
        {
            cout << "advertise" << endl;
        }
        else {
            cout << "does not matter" << endl;
        }
    }
}