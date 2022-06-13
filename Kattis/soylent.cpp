#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    float cal = 400, usin[cases], result[cases];
    for (int i = 0; i < cases; i++) {
        cin >> usin[i];
        result[i] = ceil(usin[i] / cal);
    }

    for (int i = 0; i < cases; i++) {
        cout << result[i] << endl;
    }
}