#include <iostream>

using namespace std;

int main() {
    int usin;
    cin >> usin;

    for (int i = 2; i < usin; i++) {
        if (usin % i == 0) {
            cout << "not prime" << endl;
            return 0;
        }
    }
    cout << "prime" << endl;
}