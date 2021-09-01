#include <iostream>
#include <vector>

using namespace std;

int main() {
    int c;
    vector<int> input;
    while((c = getchar()) != EOF) {
        printf("%c", char(c));
        input.push_back(char(c));
    }
}