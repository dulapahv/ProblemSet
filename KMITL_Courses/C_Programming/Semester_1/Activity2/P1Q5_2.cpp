#include <iostream>
#include <string>

using namespace std;

int main()
{
    string usin;
    cout << "Enter Text: ";
    getline(cin, usin);

    for (int i = 0; i < usin.size(); i++)
        cout << char(toupper(usin[i]));
}