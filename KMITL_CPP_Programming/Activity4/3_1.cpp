#include <iostream>

using namespace std;

int main() {
    int number[8][5];
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> number[i][j];
        }
    }

    cout << "Row totals: ";
    for (int i = 0; i < 8; i++) {
        int row = 0;
        for (int j = 0; j < 5; j++) {
            row += number[i][j];
        }
        cout << row << " ";
    }

    cout << endl << "Column totals: ";
    for (int i = 0; i < 5; i++) {
        int column = 0;
        for (int j = 0; j < 8; j++) {
            column += number[j][i];
        }
        cout << column << " ";
    }
}