/* Pseudocode */
// Create a column Fahr and Celsius
// Generate values for Fahrenheit from 300 - 0 with decremental of 20
// Convert values from Fahrenheit to Celsius
// Print values of Fahrenheit and Celsius in each column

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int fahr;
    float celsius;

    cout << "Fahr" << setw(10) << "Celsius" << endl;

    for (float i = 15; i >= 0; i--) {
        fahr = (i * 20);
        celsius = (((i * 20) - 32) * 5 / 9);
        cout << setprecision(1) << fixed << setw(3) << fahr << setw(11) << celsius << endl;
    }
}