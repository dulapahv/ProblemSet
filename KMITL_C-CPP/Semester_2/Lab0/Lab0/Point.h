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
	float x, y;

	Point() { x = y = 0.0f; }
	Point(float xa, float ya) {
		x = xa; y = ya;
	}

	float getX() { return x; }
	void setX(float x1) { x = x1; }
	float getY() { return y; }
	void setY(float y1) { y = y1; }

	// Move point by distance dv 
	void move(Point dv);
	// Calculate distance from b to this point
	float distance(Point& b);

	// Add a point to a stream
	void print(ofstream& f);
	// Add a point to the std output stream cout
	void print();
};
