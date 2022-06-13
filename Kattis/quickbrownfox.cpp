#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    cin.ignore();

    vector<char> alphabet;
    for (int i = 0; i < 26; i++) {
        alphabet.push_back(char(i + 97));
    }

    string usin;
    for (int i = 0; i < cases; i++) {
        getline(cin, usin);

        for (int j = 0; j < usin.size(); j++) {
            if (count(alphabet.begin(), alphabet.end(), usin[j])) {
                int location = usin[j];
                alphabet.erase(alphabet.begin() + location);
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        cout << alphabet[i];
    }
}