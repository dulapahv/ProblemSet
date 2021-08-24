#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int fahr;
    float celsius;

    cout << "Fahr" << setw(10) << "Celsius" << endl;

    for (float i = 0; i < 16; i++) {
        fahr = (i * 20);
        celsius = (((i * 20) - 32) * 5 / 9);
        cout << setprecision(1) << fixed << setw(3) << fahr << setw(11) << celsius << endl;
    }
}

