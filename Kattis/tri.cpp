#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    if (a + b == c) {
        cout << a << "+" << b << "=" << c << endl;
        exit(0);
    }
    else if (a - b == c) {
        cout << a << "-" << b << "=" << c << endl;
        exit(0);
    }
    else if (a * b == c) {
        cout << a << "*" << b << "=" << c << endl;
        exit(0);
    }
    else if (a / b == c) {
        cout << a << "/" << b << "=" << c << endl;
        exit(0);
    }

    if (b + c == a) {
        cout << a << "=" << b << "+" << c << endl;
        exit(0);
    }
    else if (b - c == a) {
        cout << a << "=" << b << "-" << c << endl;
        exit(0);
    }
    else if (b * c == a) {
        cout << a << "=" << b << "*" << c << endl;
        exit(0);
    }
    else if (b / c == a) {
        cout << a << "=" << b << "/" << c << endl;
        exit(0);
    }

    if (a + c == b) {
        cout << a << "=" << b << "-" << c << endl;
        exit(0);
    }
    else if (a - c == b) {
        cout << a << "=" << b << "+" << c << endl;
        exit(0);
    }
    else if (a * c == b) {
        cout << a << "=" << b << "/" << c << endl;
        exit(0);
    }
    else if (a / c == b) {
        cout << a << "=" << b << "*" << c << endl;
        exit(0);
    }

    if (b - a == c) {
        cout << a << "=" << b << "-" << c << endl;
        exit(0);
    }
    else if (c - a == b) {
        cout << a << "=" << c << "-" << b << endl;
        exit(0);
    }
    else if (c - b == a) {
        cout << a << "=" << c << "-" << b << endl;
        exit(0);
    }
}