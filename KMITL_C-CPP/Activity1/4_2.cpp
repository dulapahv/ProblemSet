// Written by Dulapah Vibulsanti (64011388)

// 4.2. Determine whether the real number given by user is positive, negative, or zero

#include <iostream>

using namespace std;

int main() {
    float usin;
    cin >> usin;

    if (usin > 0) {
        cout << "positive" << endl;
    }
    else if (usin < 0) {
        cout << "negative" << endl;
    }
    else {
        cout << "zero" << endl;
    }
}