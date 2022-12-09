#include <iostream>

using namespace std;

int main()
{
    int MB = 0;
    int months = 0;

    cin >> MB >> months;

    int used = 0;
    for (int i = 0; i < months; i++)
    {
        int daily;
        cin >> daily;
        used += daily;
    }

    cout << MB * (months + 1) - used << endl;
}