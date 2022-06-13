#include <iostream>
#include "Triangle.h"

using namespace std;

int main() {
    double x1;
    double y1;
    double x2;
    double y2;
    double x3;
    double y3;
    cout << "Please enter position X1:";
    cin >> x1;
    cout << "Please enter position y1:";
    cin >> y1;
    cout << "Please enter position X2:";
    cin >> x2;
    cout << "Please enter position y2:";
    cin >> y2;
    cout << "Please enter position X3:";
    cin >> x3;
    cout << "Please enter position y3:";
    cin >> y3;

    Triangle t1();
    Triangle t2(x1, y1, x2, y2, x3, y3);

    cout << "properties: " << endl;
    cout << "point1: (" << x1 << "," << y1 << ")" << endl;
    cout << "point1: (" << x2 << "," << y2 << ")" << endl;
    cout << "point1: (" << x3 << "," << y3 << ")" << endl;

    cout << "Area: " << t2.Area() << endl;
    cout << "Perimeter: " << t2.perimeter() << endl;

    cout << t2.isEquilateral() << endl;
    cout << t2.isIsosceles() << endl;
    cout << t2.isScalene() << endl;

    return 0;
}