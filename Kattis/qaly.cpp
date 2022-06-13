#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int x;
    cin >> x;

    float usin[x][2];
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    float result = 0;
    for (int i = 0; i < x; i++) {
        result += usin[i][0] * usin[i][1];
    }

    cout << setprecision(3) << fixed << result << endl;
}