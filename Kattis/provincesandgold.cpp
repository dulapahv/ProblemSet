#include <iostream>

using namespace std;

int main() {
    int usin[3];
    for (int i = 0; i < 3; i++) {
        cin >> usin[i];
    }

    int bp = 0;
    bp = (usin[0] * 3) + (usin[1] * 2) + (usin[2] * 1);

    string victory;
    while (bp >= 2) {
        if (bp >= 8) {
            victory = "Province";
            break;
        }
        else if (bp >= 5) {
            victory = "Duchy";
            break;
        }
        else {
            victory = "Estate";
            break;
        }
    }

    while (bp >= 0)
    {
        if ()if (bp >= 8) {
            victory = "Province";
            break;
        }
        else if (bp >= 5) {
            victory = "Duchy";
            break;
        }
        else {
            victory = "Estate";
            break;
        }
    
}