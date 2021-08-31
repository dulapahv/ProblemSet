#include <iostream>

using namespace std;

int main() {
    int number[5][5];
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> number[i][j];
        }
    }

    int result[25], x = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            result[x] = number[i][j];
            x++;
        }
    }
    
    for (int i = 0; i < 25; i++) {
        cout << result[i] << " ";
    }
}