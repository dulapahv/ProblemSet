#include <iostream>

using namespace std;

int main() {
    int usin;
    while((usin = getchar()) != EOF) {
        if (usin == '\t')
            cout << "\\t ";
        else if (usin == '\n')
            cout << "\\n ";
    }
    return 0;
}