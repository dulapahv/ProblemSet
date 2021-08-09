#include <iostream>

using namespace std;

int main() {
    int qNo;
    string ans;
    cin >> qNo >> ans;

    string adrian, bruno, goran;
    int a = 0, b = 0, g = 0;
    for (int i = 1; i < qNo; i++) {
        // adrian[(3 * i) - 3] = 'A';
        // adrian[(3 * i) - 2] = 'B';
        // adrian[(3 * i) - 1] = 'C';

        bruno[(4 * i) - 3] = 'A';
        bruno[(2 * i) - 2] = 'B';
        bruno[(4 * i) - 1] = 'C';

        // goran[(6 * i) - 4] = 'A';
        // goran[(6 * i) - 3] = 'A';
        // goran[(6 * i) - 2] = 'B';
        // goran[(6 * i) - 1] = 'B';
        // goran[(6 * i) - 6] = 'C';
        // goran[(6 * i) - 5] = 'C';
    }

    for (int i = 0; i < qNo; i++) {
        // if (a = ans[i]) {
        //     a++;
        // }
        // else if (b = ans[i]) {
        //     b++;
        // }
        // else {
        //     g++;
        // }
        cout << bruno[i];
    }

    // cout << a << " " << b << " " << g << endl;
}