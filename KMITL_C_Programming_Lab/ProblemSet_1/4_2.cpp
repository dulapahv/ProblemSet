// Written by Dulapah Vibulsanti (64011388)

// 4.2. Determine whether the real number given by user is positive, negative, or zero

#include <iostream>

using namespace std;

int main() {
    double usin;
    cin >> usin;

    if (usin > 0) {
        cout << usin << endl;
    }
    else if (usin < 0) {
        cout << "negative" << endl;
    }
    else {
        cout << "zero" << endl;
    }
}