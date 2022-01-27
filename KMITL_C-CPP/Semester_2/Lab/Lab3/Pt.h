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

template <typename T>
class Pt {
public:
	T x, y;

	Pt() { x = y = 0.0f; }
	Pt(T xa, T ya) {
		x = xa; y = ya;
	}

	T getX() { return x; }
	void setX(T x1) { x = x1; }
	T getY() { return y; }
	void setY(T y1) { y = y1; }

	// Move point by distance dv 
	void move(Pt<T> dv);
	// Calculate distance from b to this point
	T distance(Pt<T>& b);

	// Add a point to a stream
	void print(ofstream& f);
	// Add a point to the std output stream cout
	void print();
};