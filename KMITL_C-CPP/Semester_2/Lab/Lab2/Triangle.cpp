#include <ctype.h>
#include <assert.h>
#include <cmath>
#include "Triangle.h"

/* Get distance between 2 vertices */
double getEuclideanDistance(double p1x, double p1y, double p2x, double p2y) {
	return sqrt(pow((p2x - p1x), 2) + pow((p2y - p1y), 2));
}

Triangle::Triangle(double ax, double ay, double bx, double by, double cx, double cy) {
	/* Check whether the coordinates are numeric or not */
	assert(!isnan(ax) || !isnan(ay));
	assert(!isnan(bx) || !isnan(ay));
	assert(!isnan(cx) || !isnan(ay));
	p1x = ax, p1y = ay, p2x = bx, p2y = by, p3x = cx, p3y = cy;
	/* Check whether the coordinates are valid or not */
	assert(getArea() > 0 && getPerimeter() > 0);
}

Triangle::Triangle(double a1[2], double a2[2], double a3[2]) {
	/* Check whether the coordinates are numeric or not */
	assert(!isnan(a1[0]));
	assert(!isnan(a2[0]));
	assert(!isnan(a3[0]));
	p1x = a1[0]; p1y = a1[1];
	p2x = a2[0]; p2y = a2[1];
	p3x = a3[0]; p3y = a3[1];
	/* Check whether the coordinates are valid or not */
	assert(getArea() > 0 && getPerimeter() > 0);
}

/* Get coordinate of each specified vertex */
double Triangle::getp1x() { return p1x; }
double Triangle::getp1y() { return p1y; }
double Triangle::getp2x() { return p2x; }
double Triangle::getp2y() { return p2y; }
double Triangle::getp3x() { return p3x; }
double Triangle::getp3y() { return p3y; }

/* Get area of the triangle */
double Triangle::getArea() {
	return 0.5 * ((p1x * (p2y - p3y)) + (p2x * (p3y - p1y)) + (p3x * (p1y - p2y)));
}

/* Get perimeter of the triangle */
double Triangle::getPerimeter() {
	double l1, l2, l3;
	l1 = getEuclideanDistance(p1x, p1y, p2x, p2y);
	l2 = getEuclideanDistance(p2x, p2y, p3x, p3y);
	l3 = getEuclideanDistance(p3x, p3y, p1x, p1y);
	return l1 + l2 + l3;
}

/* Check if the triangle is equilateral or not */
bool Triangle::isEquilateral() {
	/* If all 3 vertices have the same distance then it is equilateral */
	double l1, l2, l3;
	l1 = getEuclideanDistance(p1x, p1y, p2x, p2y);
	l2 = getEuclideanDistance(p2x, p2y, p3x, p3y);
	l3 = getEuclideanDistance(p3x, p3y, p1x, p1y);
	if (l1 == l2 && l2 == l3 && l3 == l1)
		return true;
	else
		return false;
}

/* Check if the triangle is isosceles or not */
bool Triangle::isIsosceles() {
	/* If ONLY 2 vertices have the same distance then it is isosceles */
	double l1, l2, l3;
	l1 = getEuclideanDistance(p1x, p1y, p2x, p2y);
	l2 = getEuclideanDistance(p2x, p2y, p3x, p3y);
	l3 = getEuclideanDistance(p3x, p3y, p1x, p1y);
	if (((l1 == l2) || (l2 == l3) || (l3 == l1)) && !isEquilateral())
		return true;
	else
		return false;
}

/* Check if the triangle is scalene or not */
bool Triangle::isScalene() {
	/* If it is neither equilateral nor isosceles then it is scalene */
	if (!isEquilateral() && !isIsosceles())
		return true;
	else
		return false;
}