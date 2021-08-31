#include <iostream>

using namespace std;

int main() {
    int number[8][5];
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> number[i][j];
        }
    }

    int result[40], x = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 5; j++) {
            result[x] = number[i][j];
            x++;
        }
    }
    
    for (int i = 0; i < 40; i++) {
        cout << result[i] << " ";
    }
}