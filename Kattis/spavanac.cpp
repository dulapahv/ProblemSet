#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int h, m, total = 0;
    cin >> h >> m;

    if (m < 45 && h == 0) {
        h += 24;
    }

    total = ((h * 60) + m) - 45;
    h = floor(total / 60);
    m = total % 60;

    cout << h << " " << m << endl;
}