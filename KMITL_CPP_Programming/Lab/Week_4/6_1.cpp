#include <iostream>
#include <math.h>

using namespace std;

int main() {
    FILE* file = fopen("6_1.txt", "r");
    float temp, sum = 0, temp2;
    int i = 0;
    char *end;
    for (char c; (c = fgetc(file)) != EOF;) {
        if (c == '.' || c == '\n')
            continue;
        temp = strtod(&c, &end);
        cout << temp;
        cout << *end;


        
    }
    cout << temp;

    fclose(file);
}