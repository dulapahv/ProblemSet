#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int cities;
    char usin[20];
    string name;
    for (int i = 0; i < cases; i++) {
        cin >> cities;

        for (int j = 0; j < cities; j++) {
            cin >> usin;
            name += usin;
        }
    }

    cout << name;
}