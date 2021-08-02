#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        string usin;
        char bank[26] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};

        getsline(cin >> usin);
        
        for (int j = 0; j < sizeof(usin); j++) {
            if (usin[j] == bank)
        }
    }
}