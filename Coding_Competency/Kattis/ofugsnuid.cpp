#include <iostream>

using namespace std;

int main() {
    int number;
    cin >> number;

    int usin[number];
    for (int i = 0; i < number; i++) {
        cin >> usin[i];
    }

    for (int i = number - 1; i >= 0; i--) {
        cout << usin[i] << endl;
    }
}