#include <iostream>
#include <string>

using namespace std;

int main()
{
    string usin;
    getline(cin, usin);

    for (int i = 0; i < usin.size(); i++)
        cout << char(tolower(usin[i]));
}