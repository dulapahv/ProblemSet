#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    for (int i = a; i < b; i++) {
        if (i == c) {
            //cout << i << endl;
            break;
        }
        else if (floor(i / 10) + (i % 10) == c) {
            //cout << i << endl;
            break;
        }
        else if (floor(i / 100) + floor((i / 10) % 10) + (i % 10) == c) {
            cout << i << endl;
            break;
        }
        else if (floor(i / 1000) + floor(i / 100) + floor(i / 10) + (i % 10) == c) {
            //cout << i << endl;
            break;
        }
        else if (floor(i / 10000) + floor(i / 1000) + floor(i / 100) + floor(i / 10) + (i % 10) == c) {
            //cout << i << endl;
            break;
        }
    }
}