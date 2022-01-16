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
#include <math.h>

using namespace std;

#include "C:\Users\Dulapah Vibulsanti\OneDrive\Documents\GitHub\ProblemSet\KMITL_C-CPP\Semester_2\Lab\Lab1\header\Pt.h"

template <typename T>
void Pt<T>::move(Pt<T> dx) {
		x = x + dx.x; y = y + dx.y;
	}

template <typename T>
T Pt<T>::distance(Pt<T> &b) {
	double d;
	double dx = b.x - x;
	double dy = b.y - y;
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
