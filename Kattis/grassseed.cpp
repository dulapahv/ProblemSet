#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    float cost;
    cin >> cost;

    int cases;
    cin >> cases;

    float usin[cases][2];
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    float area = 0;
    for (int i = 0; i < cases; i++) {
        area += usin[i][0] * usin[i][1];
    }

    float result = 0;
    result = area * cost;

    cout << setprecision(7) << fixed << result;
}