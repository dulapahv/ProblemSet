#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int fahr;
    float celsius;

    cout << "Fahr" << setw(10) << "Celsius" << endl;

    for (float i = 0; i < 8; i++) {
        fahr = (i * 40);
        celsius = (((i * 40) - 32) * 5 / 9);
        cout << setprecision(1) << fixed << setw(3) << fahr << setw(11) << celsius << endl;
    }
}