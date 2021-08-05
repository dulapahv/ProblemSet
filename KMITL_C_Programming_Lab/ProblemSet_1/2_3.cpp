#include <iostream>

#define PI 3.1416

using namespace std;

int main() {
    float r[] = {1.5, 2.2, 3.5, 4.2}; // Specify desired radius here

    for (int i = 0; i < sizeof(r)/sizeof(r[0]); i++) {
        cout << "The area of a circle of radius " << r[i] << " is " << PI * r[i] * r[i] << endl;
    }
}