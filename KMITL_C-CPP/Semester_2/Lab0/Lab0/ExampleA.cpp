// ExampleA.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "Rectangle.h"

using namespace std;

extern bool VectorExampleA();
extern bool VectorExampleString();

int main()
{
    cout << "Hello World!\n";

    cout << "Size of char " << sizeof(char) << " bytes" << endl;
    cout << "Size of bool " << sizeof(bool) << " bytes" << endl;

    cout << "Size of short int " << sizeof(short int) << " bytes" << endl;
    cout << "Size of int " << sizeof(int) << " bytes" << endl;
    cout << "Size of long int " << sizeof(long int) << " bytes" << endl;
    cout << "Size of long long " << sizeof(long long) << " bytes" << endl;
    cout << "Size of pointer " << sizeof(int*) << " bytes" << endl;
    cout << "Size of Rectangle " << sizeof(Rectangle) << " bytes" << endl;

    float x1, x2, y1, y2;
    cout << "Enter rectangle tl ";
    cin >> x1; cin >> y1;
    cout << "br ";
    cin >> x2; cin >> y2;
    Rectangle* r1 = new Rectangle(x1, y1, x2, y2);
    cout << "Area = " << r1->getArea() << endl;
    cout << "Perimeter = " << r1->getPerimeter() << endl;
    cout << "Move this rectangle ";
    float dx, dy;
    cin >> dx; cin >> dy;
    r1->move(dx, dy);
    Point tlr = r1->getTL();
    cout << "Top left is now " << tlr.x << ", " << tlr.y << endl;

    /**  Write to a file **/
    ofstream myfile;
    myfile.open("D:\\tmp\\example.txt");
    myfile << "Test text in a file" << endl;
    myfile << "Point ";  tlr.print(myfile); myfile << endl;
    myfile.close();

    //string s("Test string");
    //string sub = s.

    bool ok = VectorExampleA();
    ok = VectorExampleString();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
