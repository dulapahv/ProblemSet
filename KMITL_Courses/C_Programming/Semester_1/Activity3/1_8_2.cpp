/* Pseudocode */
// Create 2 columns, Celsius and Fahr
// Generate values for Celsius from 0 - 280 with incremental of 40
// Define a function to convert values from Celsius to Fahrenheit
// Print values of Celsius and Fahrenheit in each column

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

    for (float i = 0; i < 8; i++) {
        celsius = (i * 40);
        cout << setprecision(1) << fixed << setw(7) << celsius << setw(11) << c_to_f(celsius) << endl;
    }
}