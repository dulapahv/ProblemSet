#include <iostream>

using namespace std;

int main() {
    int w, n = 0;
    cin >> w >> n;

    int usin[n][2];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    int area, l = 0;
    for (int i = 0; i < n; i++) {
        area += usin[i][0] * usin[i][1];
    }

    l = area / w;

    cout << l << endl;
}