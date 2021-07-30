#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int usin[10];
    for (int i = 0; i < 10; i++) {
        cin >> usin[i];
        usin[i] %= 42;
    }

    int x = sizeof(usin) / sizeof(usin[0]);
    sort(usin, usin + x);

    int a = 10;
    for (int i = 1; i < 10; i++) {
        if (usin[i-1] == usin[i]) {
            a -= 1;
        }
    }

    cout << a << endl;
}