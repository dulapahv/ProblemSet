#include <iostream>


using namespace std;

void ff(int y[], int s) {
    int r;
    for (int i = 0; i < s; i++) {
        r = 1;
        for (int j = 1; j <= i; j++)
            r *= j;
        y[i] = r;
    }
    return;
}

int main()
{
    const int size = 7;
    int a[size];
    int x;

    ff(a, size);
    cout << "Enter a number between 0-6: ";
    cin >> x;
    cout << a[x];
}