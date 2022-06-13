// Written by Dulapah Vibulsanti (64011388)

// 1.2. Find circumference from the given radius (1.5, 2.2)

#include <iostream>

#define PI 3.1416

using namespace std;

int main() {
    float r[] = {1.5, 2.2}; // Specify desired radius here

    for (int i = 0; i < sizeof(r)/sizeof(r[0]); i++) {
        cout << "The circumference of a circle of radius " << r[i] << " is " << 2 * PI * r[i] << endl;
    }
}