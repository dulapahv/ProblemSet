#include <iostream>

using namespace std;

int main() {
    int usin[3];
    for (int i = 0; i < 3; i++) {
        cin >> usin[i];
    }

    for (int i = 1; i <= usin[2]; i++) {
        if (i % usin[0] == 0 && i % usin[1] == 0) {
            cout << "FizzBuzz" << endl;
        }
        else if (i % usin[0] == 0) {
            cout << "Fizz" << endl;
        }
        else if (i % usin[1] == 0) {
            cout << "Buzz" << endl;
        }
        else {
            cout << i << endl;
        }
    }
}