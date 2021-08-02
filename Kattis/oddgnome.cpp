#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int gnomeNum;
    for (int i = 0; i < cases; i++) {
        cin >> gnomeNum;

        int usin[gnomeNum];
        for (int j = 0; j < gnomeNum; j++) {
            cin >> usin[j];
        }
    }

    for (int i = 1; i < gnomeNum - 1; i++) {
        if (usin[i] > usin[i-1] && usin[i] > usin[i+1]) {
            cout << i << endl;
            exit(0);
        }
        else if (usin[i] < usin[i-1] && usin[i] < usin[i+1]) {
            cout << i << "2nd" << endl;
            exit(0);
        }
    }

}