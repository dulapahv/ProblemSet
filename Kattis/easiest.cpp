#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<int> usin;
    int temp = 1;
    while (temp != 0) {
        cin >> temp;
        if (temp != 0) {
            usin.push_back(temp);
        }
    }

    for (int i = 0; i < usin.size(); i++) {
        int m = 0, prod = 0, sum = 0;
        while(true) {
            prod = m * usin[i];
            for (int j = 0; j < to_string(prod).length(); j++) {
                sum += prod[j];
            }
        }
    }

    
}