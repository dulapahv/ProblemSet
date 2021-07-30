#include <iostream>

using namespace std;

int main() {
    int usin[3];
    for (int i = 0; i < 3; i++) {
        cin >> usin[i];
    }

    int x = usin[0], y = usin[1], z = usin[2], result = 0;
    result = max(x - y, y) * max(x - z, z) * 4;

    cout << result << endl;
}