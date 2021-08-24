#include <iostream>
#include <iomanip>

using namespace std;

float c_to_f(int celsius) {
    float fahr = (((celsius) * 9 / 5) + 32);
    return fahr;
}

int main() {
    float fahr;
    int celsius;

    cout << "Celsius" << setw(11) << "Fahr" << endl;

    for (float i = 0; i < 16; i++) {
        celsius = (i * 20);
        cout << setprecision(1) << fixed << setw(7) << celsius << setw(11) << c_to_f(celsius) << endl;
    }
}