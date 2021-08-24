#include <iostream>

using namespace std;

int main() {
    FILE* file = fopen("6_1.txt", "r");
    int sum = 0;
    for (int c; (c = fgetc(file)) != EOF;) {
        char temp = strtod(c, &end);
        cout <<  << endl;
    }

    fclose(file);
}