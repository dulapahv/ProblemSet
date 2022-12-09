#include <iostream>

using namespace std;

int main()
{
    int x, y;
    while (cin >> x >> y) {
        if (x > 0) {
            if (y > 0) {
                cout << 1 << endl;
            }
            else {
                cout << 4 << endl;
            }
        }
        else {
            if (y > 0) {
                cout << 2 << endl;
            }
            else {
                cout << 3 << endl;
            }
        }
    }
}