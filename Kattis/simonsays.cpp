#include <iostream>
#include <string>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    cin.ignore();

    for (int i = 0; i < cases; i++) {
        string usin;
        getline(cin, usin);
        if (usin.find("Simon says") == 0) { // If found Simon says
            usin.erase(0,11); // Remove "Simon says " (11 char)
            cout << usin << endl;
        }
    }
}