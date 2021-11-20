/* Pseudocode */
// Create 2 columns, Fahr and Celsius
// Generate values for Fahrenheit from 0 - 280 with incremental of 40
// Convert values from Fahrenheit to Celsius
// Print values of Fahrenheit and Celsius in each column

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