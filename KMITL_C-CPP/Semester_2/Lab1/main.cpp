/*
Test cases for:

1. Equilateral Triangle
Vertex 1 - (1.2, 5.148)
Vertex 2 - (-3.1, -2.3)
Vertex 3 - (5.5, -2.3)

2. Isoscles Triangle
Vertex 1 - (-1.2, -3.5)
Vertex 2 - (5.2, -3.5)
Vertex 3 - (2, 7.265)

3. Scalene Triangle
Vertex 1 - (-2.6, 1.2)
Vertex 2 - (5.2, 1.7)
Vertex 3 - (0.78, 7.13)

4. Invalid Triangle (area <= 0 or perimeter <= 0)
Vertex 1 - (1, 2)
Vertex 2 - (3, 4)
Vertex 3 - (5, 6)  // Program terminates

5. Invalid Input (not numeric)
Vertex 1 - (1, a)  // Program terminates
*/

#include <iostream>
#include "Triangle.h"

using namespace std;

int main() {
	/* Creating a triangle object from user-input coordinates of 3 vertices */
	double p1x, p1y, p2x, p2y, p3x, p3y;
	cout << "Enter x-coordinate for vertex 1/3: ";
	cin >> p1x;
	cout << "Enter y-coordinate for vertex 1/3: ";
	cin >> p1y;
	cout << "Enter x-coordinate for vertex 2/3: ";
	cin >> p2x;
	cout << "Enter y-coordinate for vertex 2/3: ";
	cin >> p2y;
	cout << "Enter x-coordinate for vertex 3/3: ";
	cin >> p3x;
	cout << "Enter y-coordinate for vertex 3/3: ";
	cin >> p3y;
	cout << endl;

	Triangle* t = new Triangle(p1x, p1y, p2x, p2y, p3x, p3y);

	/* Creating a triangle object from 3 arrays of vertex coordinates */
	/*
	double p1[] = {1.2, 5.148};
	double p2[] = {-3.1, -2.3};
	double p3[] = {5.5, -2.3};

	Triangle* t1 = new Triangle(p1, p2, p3);
	*/

	/* Displaying the triangle property. */
	cout << "Triangle properties:" << endl;

	cout << "Vertex 1: (" << t->getp1x() << ", " << t->getp1y() << ")" << endl;
	cout << "Vertex 2: (" << t->getp2x() << ", " << t->getp2y() << ")" << endl;
	cout << "Vertex 3: (" << t->getp3x() << ", " << t->getp3y() << ")" << endl;

	cout << "Area: " << t->getArea() << " px^2" << endl;
	cout << "Perimeter " << t->getPerimeter() << " px" << endl;

	cout << boolalpha;
	cout << "Is equilateral? " << t->isEquilateral() << endl;
	cout << "Is isosceles? " << t->isIsosceles() << endl;
	cout << "Is scalene? " << t->isScalene() << endl;

	delete t;
	return 0;
}