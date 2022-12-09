#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    float usin[cases][5];
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> usin[i][j];
        }
    }

    
    float t = 0, y[cases];
    for (int i = 0; i < cases; i++) {
        t = usin[i][2] / (usin[i][0] * cos(usin[i][1] * 3.14 / 180));
        y[i] = (usin[i][0] * t * sin(usin[i][1] * 3.14 / 180)) - (0.5 * 9.81 * (t*t));
        
    } 

    for (int i = 0; i < cases; i++) {
        usin[i][3] += 1;
        usin[i][4] -= 1;
        if (y[i] > usin[i][3] && y[i] < usin[i][4]) {
            cout << "Safe" << endl;
        }
        else {
            cout << "Not Safe" << endl;
        }
    }
}