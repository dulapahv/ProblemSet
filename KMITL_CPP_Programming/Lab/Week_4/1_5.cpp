#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    float fahr;
    int celsius;

    cout << "Celsius" << setw(11) << "Fahr" << endl;

    for (float i = 0; i < 8; i++) {
        fahr = (((i * 40) * 9 / 5) + 32);
        celsius = (i * 40);
        cout << setprecision(1) << fixed << setw(7) << celsius << setw(11) << fahr << endl;
    }
}