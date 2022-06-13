#include <iostream>

using namespace std;

int main() {
    int usin[3];
    for (int i = 0; i < 3; i++) {
        cin >> usin[i];
    }

    int result = 1;
    for (int i = 0; i < 3; i++) {
        result *= usin[i];
    }

    cout << result << endl;
}