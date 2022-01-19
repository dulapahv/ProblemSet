#include <ctype.h>
#include <cmath>
#include "assert.h"
#include "Triangle.h"

Triangle::Triangle(double a1x, double a1y, double b2x, double b2y, double c3x, double c3y) {
	p1x = a1x, p1y = a1y, p2x = b2x, p2y = b2y, p3x = c3x, p3y = c3y;
}

Triangle::Triangle(double a1[2], double a2[2], double a3[2]) {
	p1x = a1[0]; p1y = a1[1];
	p2x = a2[0]; p2y = a2[1];
	p3x = a3[0]; p3y = a3[1];
}

double Triangle::getp1x() { return p1x; }
double Triangle::getp1y() { return p1y; }
double Triangle::getp2x() { return p2x; }
double Triangle::getp2y() { return p2y; }
double Triangle::getp3x() { return p3x; }
double Triangle::getp3y() { return p3y; }

double Triangle::getArea() {
	return 0.5 * ((p1x * (p2y - p3y)) + (p2x * (p3y - p1y)) + (p3x * (p1y - p2y)));
}

double Triangle::getPerimeter() {
	double l1, l2, l3;
	l1 = sqrt(pow((p2x - p1x), 2) + pow((p2y - p1y), 2));
	l2 = sqrt(pow((p3x - p2x), 2) + pow((p3y - p2y), 2));
	l3 = sqrt(pow((p3x - p1x), 2) + pow((p3y - p1y), 2));
	return l1 + l2 + l3;
}

bool Triangle::isEquilateral() {
	double l1, l2, l3;
	l1 = sqrt(pow((p2x - p1x), 2) + pow((p2y - p1y), 2));
	l2 = sqrt(pow((p3x - p2x), 2) + pow((p3y - p2y), 2));
	l3 = sqrt(pow((p3x - p1x), 2) + pow((p3y - p1y), 2));
	if (l1 == l2 && l2 == l3 && l3 == l1)
		return true;
	else
		return false;
}

bool Triangle::isIsosceles() {
	double l1, l2, l3;
	l1 = sqrt(pow((p2x - p1x), 2) + pow((p2y - p1y), 2));
	l2 = sqrt(pow((p3x - p2x), 2) + pow((p3y - p2y), 2));
	l3 = sqrt(pow((p3x - p1x), 2) + pow((p3y - p1y), 2));
	if (((l1 == l2) || (l2 == l3) || (l3 == l1)) && !isEquilateral())
		return true;
	else
		return false;
}

bool Triangle::isScalene() {
	if (!isEquilateral() && !isIsosceles())
		return true;
	else
		return false;
}