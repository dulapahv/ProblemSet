#include <iostream>
#include <string>

using namespace std;

int main() {
    string usin1, usin2, usin3, usin4;
    string name1 = "Warrior: ", name2 = "Mage: ", name3 = "Ninja: ", name4 = "Fighter: ";
    cout << "Enter 4 names: ";
    cin >> usin1 >> usin2 >> usin3 >> usin4;

    name1.append(usin1);
    name2.append(usin2);
    name3.append(usin3);
    name4.append(usin4);

    int maxLen = name1.length();
    if (name2.length() > maxLen) maxLen = name2.length();
    if (name3.length() > maxLen) maxLen = name3.length();
    if (name4.length() > maxLen) maxLen = name4.length();

    cout << string(maxLen + 4, '*') << endl;
}