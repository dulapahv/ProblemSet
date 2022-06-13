#include <iostream>

using namespace std;

int main() {
    int usin[3];
    for (int i = 0; i < 3; i++) {
        cin >> usin[i];
    }

    int x = (usin[0] * 3) + (usin[1] * 2) + (usin[2] * 1);

    string victory;
    while (x >= 2) {
        if (x >= 8) {
            victory = "Province or ";
            break;
        }
        else if (x >= 5) {
            victory = "Duchy or ";
            break;
        }
        else {
            victory = "Estate or ";
            break;
        }
    }

    string treasure;
    while (x >= 0)
    {
        if (x >= 6) {
            treasure = "Gold";
            break;
        }
        else if (x >= 3) {
            treasure = "Silver";
            break;
        }
        else {
            treasure = "Copper";
            break;
        }
    }
    
    cout << victory << treasure << endl;
}