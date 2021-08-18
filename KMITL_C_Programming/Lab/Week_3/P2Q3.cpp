#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int height;
    cin >> height;

    if (height % 2 == 0)
        height = (height / 2) + 1; 
    else
        height = floor(height / 2);

    int space = height - 1;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= space; j++)
            cout << " ";
        space--;
        for (int j = 1; j <= (2 * i - 1); j++)
            cout << "*";
        cout << endl;
    }

    space = 1;
    for (int i = 1; i <= (height - 1); i++) {
        for (int j = 1; j <= space; j++)
            cout << " ";
        space++;
        for (int j = 1; j <= (2 * (height - i) - 1); j++)
            cout << "*";
        cout << endl;
    }
}