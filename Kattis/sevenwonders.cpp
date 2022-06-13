#include <iostream>
#include <string.h>

using namespace std;

int main() {
    char input[51];
    cin >> input;

    int c = 0, g = 0, t = 0;
    for (int i = 0; i < strlen(input); i++) {
        if (input[i] == 'C') {
            c++;
        }
        else if (input[i] == 'G') {
            g++;
        } 
        else if (input[i] == 'T') {
            t++;
        }
    }
    int score = ((c * c) + (g * g) + (t * t));
    if (c != 0 && g != 0 && t != 0) {
        int min = c;
        if (g < min) {
            min = g;
        }
            
        if (t < min) {
            min = t;
        }
        score += (min * 7);
    }

    cout << score << endl;
}
