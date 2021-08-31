#include <iostream>

using namespace std;

int main() {
    int number[3][5];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> number[i][j];
        }
    }

    cout << "Row totals: ";
    for (int i = 0; i < 3; i++) {
        int row = 0;
        for (int j = 0; j < 5; j++) {
            row += number[i][j];
        }
        cout << row << " ";
    }

    cout << endl << "Column totals: ";
    for (int i = 0; i < 5; i++) {
        int column = 0;
        for (int j = 0; j < 3; j++) {
            column += number[j][i];
        }
        cout << column << " ";
    }
}