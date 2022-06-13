/** Point class **/

/** This is a very simple class and programs would often
	want to manipulate the attributes directly
	So there are no private attributes ..
	there is only a Point.h file .. C++ allows the implementations in
	header files ..
	violating the information hiding principle -
	acceptable for THIS SIMPLE CASE only
	**/
#pragma once

#include <iostream>
#include <fstream>


using namespace std;

class Point {
public:
	double x, y;

	Point() { x = y = 0.0f; }
	Point(double xa, double ya) {
		x = xa; y = ya;
	}

	double getX() { return x; }
	void setX(double x1) { x = x1; }
	double getY() { return y; }
	void setY(double y1) { y = y1; }
	void move(Point dx);
	double distance(Point& b);
	void print(ofstream& f);
	void print();
};
