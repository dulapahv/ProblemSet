#include <iostream>
#include <math.h>

# define M_PI 3.14159265358979323846  /* pi */

using namespace std;

int main() {
    int usin[2];
    for (int i = 0; i < 2; i++) {
        cin >> usin[i];
    }

    double result = ceil(usin[0] / sin(usin[1] * M_PI / 180));

    cout << result << endl;
}