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

using namespace std;

#include "Pt.h"

template <typename T>
void Pt<T>::move(Pt<T> dx) {
	x = x + dx.x; y = y + dx.y;
}

template <typename T>
Pt<T> Pt<T>::operator+(Pt<T> b) {
	Pt<T> c;
	c.x = x + b.x;
	c.y = y + b.y;
	return c;
}
template <typename T>
T Pt<T>::distance(Pt<T>& b) {
	double d;
	double dx = (double)(b.x - x);
	double dy = (double)(b.y - y);
	d = sqrt(dx * dx + dy * dy);
	return (float)d;
}

template <typename T>
void Pt<T>::print(ofstream& f) {
	f << '(' << x << ',' << y << ')';
}

template <typename T>
void Pt<T>::print() {
	cout << '(' << x << ',' << y << ')';
}

template class Pt<float>;
template class Pt<double>;