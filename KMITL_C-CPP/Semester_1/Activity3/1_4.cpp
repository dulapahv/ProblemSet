/* Pseudocode */
// Create 2 columns, Celsius and Fahr
// Generate values for Celsius from 0 - 300 with incremental of 20
// Convert values from Celsius to Fahrenheit
// Print values of Celsius and Fahrenheit in each column

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    float fahr;
    int celsius;

    cout << "Celsius" << setw(11) << "Fahr" << endl;

    for (float i = 0; i < 16; i++) {
        fahr = (((i * 20) * 9 / 5) + 32);
        celsius = (i * 20);
        cout << setprecision(1) << fixed << setw(7) << celsius << setw(11) << fahr << endl;
    }
}