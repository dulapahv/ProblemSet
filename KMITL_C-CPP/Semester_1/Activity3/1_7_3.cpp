/* Pseudocode */
// Create 2 columns, Fahr and Celsius
// Generate values for Fahrenheit from 300 - 0 with decremental of 20
// Define a function to convert values from Fahrenheit to Celsius
// Print values of Fahrenheit and Celsius in each column

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

    for (float i = 15; i >= 0; i--) {
        fahr = (i * 20);
        cout << setprecision(1) << fixed << setw(3) << fahr << setw(11) << f_to_c(fahr) << endl;
    }
}