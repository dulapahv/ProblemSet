#include <iostream>

using namespace std;

int main()
{
    int amount;
    int i;
    cin >> i; // Get input
    for (i = 1; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            amount += i;
        }
    }
    cout << amount; // Output
}