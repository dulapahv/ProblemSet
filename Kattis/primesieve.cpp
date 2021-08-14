#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int x, y;
    cin >> x >> y;

    // int z;
    // for (int i = 0; i < y; i++) {
    //     cin >> z;
    // }

    int check = sqrt(x);
    for (int i = 2; i < check; i++) {
        if (x % i == 0) {
            cout << i << endl;
            break;
        }
    }
    

    // for (int i = 0; i < y; i++) {

    // }
}