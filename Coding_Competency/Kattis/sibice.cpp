#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int usin[a];
    for (int i = 0; i < a; i++) {
        cin >> usin[i];
    }

    float size = sqrt(pow(b, 2) + pow(c, 2));
    for (int i = 0; i < a; i++) {
        if (usin[i] <= size) {
            cout << "DA" << endl;
        }
        else {
            cout << "NE" << endl;
        }
    }
}