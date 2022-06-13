// Written by Dulapah Vibulsanti (64011388)

// 4.1. Determine whether the integer given by user is positive, negative, or zero

#include <iostream>

using namespace std;

int main() {
    int usin;
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