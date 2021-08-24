#include <iostream>
#include <iomanip>

using namespace std;

float f_to_c(int fahr) {
    float celsius = (((fahr) - 32) * 5 / 9);
    return celsius;
}

int main() {
    int fahr;
    float celsius;

    cout << "Fahr" << setw(10) << "Celsius" << endl;

    for (float i = 0; i < 8; i++) {
        fahr = (i * 40);
        cout << setprecision(1) << fixed << setw(3) << fahr << setw(11) << f_to_c(fahr) << endl;
    }
}