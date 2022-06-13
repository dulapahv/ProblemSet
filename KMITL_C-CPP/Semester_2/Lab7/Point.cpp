/** Point class **/

/** This is a very simple class and programs would often
	want to manipulate the attributes directly
	So there are no private attributes ..
	there is only a Point.h file .. C++ allows the implementations in
	header files ..
	violating the information hiding principle -
	acceptable for THIS SIMPLE CASE only
	**/
	// #pragma once

#include <iostream>
#include "math.h"

using namespace std;

#include "Point.h"

void Point::move(Point dx) {
	x = x + dx.x; y = y + dx.y;
}

double Point::distance(Point& b) {
	double d;
	double dx = b.x - x;
	double dy = b.y - y;
	d = sqrt(dx * dx + dy * dy);
	return (float)d;
}

void Point::print(ofstream& f) {
	f << '(' << x << ',' << y << ')';
}
void Point::print() {
	cout << '(' << x << ',' << y << ')';
}

