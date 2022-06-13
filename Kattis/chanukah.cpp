#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int usin[cases][2];
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    int result[cases];
    for (int i = 0; i < cases; i++) {
        int candles = 0;
        for (int j = 1; j <= usin[i][1]; j++) {
            candles += j;
        }

        result[i] = candles + usin[i][1];
    }

    for (int i = 0; i < cases; i++) {
        cout << i+1 << " " << result[i] << endl;
    }
}