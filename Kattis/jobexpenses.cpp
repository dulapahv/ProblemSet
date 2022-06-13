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
    for (int i = 0; i < cases; i++) {
        if (usin[i] < 0) {
            result += abs(usin[i]);
        }
    }

    cout << result << endl;
}