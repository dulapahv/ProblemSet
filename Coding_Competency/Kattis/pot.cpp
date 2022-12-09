#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int x;
    cin >> x;

    int usin[x];
    for (int i = 0; i < x; i++) {
        cin >> usin[i];
    }

    int result = 0;
    for (int i = 0; i < x; i++) {
        result += pow(int(floor(usin[i] / 10)), (usin[i] % 10));
    }

    cout << result << endl;
}