#include "Triangle.h"

int main() {
	double p1x, p1y, p2x, p2y, p3x, p3y;
	cout << "Enter x-coordinate for point 1/3: ";
	cin >> p1x;
	cout << "Enter y-coordinate for point 1/3: ";
	cin >> p1y;
	cout << "Enter x-coordinate for point 2/3: ";
	cin >> p2x;
	cout << "Enter y-coordinate for point 2/3: ";
	cin >> p2y;
	cout << "Enter x-coordinate for point 3/3: ";
	cin >> p3x;
	cout << "Enter y-coordinate for point 3/3: ";
	cin >> p3y;

	Triangle* t1 = new Triangle(p1x, p1y, p2x, p2y, p3x, p3y);
	
	cout << "\nTriangle properties:" << endl;

	cout << "Vertex 1: (" << t1->getp1x() << ", " << t1->getp1y() << ")" << endl;
	cout << "Vertex 2: (" << t1->getp2x() << ", " << t1->getp2y() << ")" << endl;
	cout << "Vertex 3: (" << t1->getp3x() << ", " << t1->getp3y() << ")" << endl;

	cout << "Area: " << t1->getArea() << " px^2" << endl;
	cout << "Perimeter " << t1->getPerimeter() << " px" << endl;

	cout << boolalpha;
	cout << "Is equilateral? " << t1->isEquilateral() << endl;
	cout << "Is isosceles? " << t1->isIsosceles() << endl;
	cout << "Is scalene? " << t1->isScalene() << endl;

	return 0;
}