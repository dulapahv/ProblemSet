#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int usin[cases];
    for (int i = 0; i < cases; i++) {
        cin >> usin[i];
    }

    int result = 0;
    if (cases & 1) {
        cout << "still running" << endl;
    }
    else {
        result = usin[1] - usin[0];
        for (int i = 2; i < cases; i++) {
            result = usin[i] - result;
        }

        cout << result << endl;
    }
}