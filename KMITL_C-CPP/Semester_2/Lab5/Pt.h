/** Template Point class **/

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

	T getX() { return x;  }
	void setX(T x1) { x = x1;  }
	T getY() { return y; }
	void setY(T y1) { y = y1; }
	
	// Move point by distance dv 
	void move(Pt<T> dv);
	Pt<T> operator+(Pt<T> b);
	// Calculate distance from b to this point
	T distance(Pt<T> &b);
	
	// Add a point to a stream
	void print(ofstream& f);
	// Add a point to the std output stream cout
	void print();
};