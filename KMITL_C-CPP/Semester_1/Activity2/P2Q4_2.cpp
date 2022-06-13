#include <iostream>

using namespace std;

void print_checker(char c1, char c2, int w, int h, int size) {
    int countHeight = 0;
    int countWidth = 0;
    for (int i = 0; i < h; i++) {
        countHeight %= (size * 2);
        for (int j = 0; j < w; j++) {
            if (countHeight < size) {
                if (countWidth < size) {
                    cout << c1;
                    countWidth++;
                }
                else {
                    cout << c2;
                    countWidth++;
                }
            }
            else {
                if (countWidth < size) {
                    cout << c2;
                    countWidth++;
                }
                else {
                    cout << c1;
                    countWidth++;
                }
            }
            countWidth %= (size * 2);
        }
        countWidth = 0;
        cout << endl;
        countHeight += 1;
    }
}

int main()
{
    int width, height, size;
    char usinChar1, usinChar2;
    cout << "Width: ";
    cin >> width;
    cout << "Height: ";
    cin >> height;
    cout << "Character 1: ";
    cin >> usinChar1;
    cout << "Character 2: ";
    cin >> usinChar2;
    cout << "Size: ";
    cin >> size;
    print_checker(usinChar1, usinChar2, width, height, size);
}