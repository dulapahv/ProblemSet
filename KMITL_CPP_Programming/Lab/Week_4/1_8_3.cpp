/* Pseudocode */
// Create a column Celsius and Fahr
// Generate values for Celsius from 300 - 0 with decremental of 20
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

    for (float i = 15; i >= 0; i--) {
        celsius = (i * 20);
        cout << setprecision(1) << fixed << setw(7) << celsius << setw(11) << c_to_f(celsius) << endl;
    }
}