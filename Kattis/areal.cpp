#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
    long double x = 0;
    cin >> x;

    cout << setprecision(20) << fixed << sqrt(x) * 4 << endl;
}