/** PointND class **/

#include <assert.h>
#include <fstream>
#include <iostream>
#include <limits>
#include <vector>
#include "assert.h"
#include "math.h"

using namespace std;

#include "PointND.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"
#include "QuadrantException.h"
#include "UnderflowException.h"

template <typename T>
int PointND<T>::XLIMIT = 500;

template <typename T>
int PointND<T>::YLIMIT = 500;

template <typename T>
unsigned int PointND<T>::size() {
	return x.size();
}

/** + operator method **/
/* Element-wise addition */
template <typename T>
inline PointND<T> PointND<T>::operator+(PointND<T>& p) {
	assert(x.size() == p.size());  // Check whether 2 points have the same dimensions

	vector<T> p1(p.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < p.size(); i++) {
		if ((p.x[i] > 0) && (x[i] > numeric_limits<T>::max() - p.x[i])) { throw OverflowException(); }  // overflow
		if ((p.x[i] < 0) && (x[i] < numeric_limits<T>::lowest() - p.x[i])) { throw UnderflowException(); }  // underflow

		p1[i] = x[i] + p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* Scalar addition */
template <typename T>
inline PointND<T> PointND<T>::operator+(T s) {
	vector<T> p1(x.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < x.size(); i++) {
		if ((s > 0) && (x[i] > numeric_limits<T>::max() - s)) { throw OverflowException(); }  // overflow
		if ((s < 0) && (x[i] < numeric_limits<T>::lowest() - s)) { throw UnderflowException(); }  // underflow

		p1[i] = x[i] + s;
	}
	
	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < x.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}


/** - operator method **/
/* Element-wise subtraction */
template <typename T>
inline PointND<T> PointND<T>::operator-(PointND<T>& p) {
	assert(x.size() == p.size());  // Check whether 2 points have the same dimensions
	
	vector<T> p1(p.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < p.size(); i++) {
		if ((p.x[i] < 0) && (x[i] > numeric_limits<T>::max() + p.x[i])) { throw OverflowException(); }  // overflow
		if ((p.x[i] > 0) && (x[i] < numeric_limits<T>::lowest() + p.x[i])) { throw UnderflowException(); }  // underflow

		p1[i] = x[i] - p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* Scalar subtraction */
template <typename T>
inline PointND<T> PointND<T>::operator-(T s) {
	vector<T> p1(x.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < x.size(); i++) {
		if ((s < 0) && (x[i] > numeric_limits<T>::max() + s)) { throw OverflowException(); }  // overflow
		if ((s > 0) && (x[i] < numeric_limits<T>::lowest() + s)) { throw UnderflowException(); }  // underflow
	
		p1[i] = x[i] - s;
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < x.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}


/** * operator method **/
/* Element-wise multiplication */
template <typename T>
inline PointND<T> PointND<T>::operator*(PointND<T>& p) {
	assert(x.size() == p.size());  // Check whether 2 points have the same dimensions
	
	vector<T> p1(p.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < p.size(); i++) {
		if ((p.x[i] == -1) && (x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if ((x[i] == -1) && (p.x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if (p.x[i] > numeric_limits<T>::max() / x[i]) { throw OverflowException(); }  // overflow
		if ((p.x[i] < numeric_limits<T>::lowest() / x[i])) { throw UnderflowException(); }  // underflow

		p1[i] = x[i] * p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* Scalar multiplication */
template <typename T>
inline PointND<T> PointND<T>::operator*(T s) {
	vector<T> p1(x.size());  // initialize vector to store answer

	/* Check for overflow of given data type then compute the result */
	for (int i = 0; i < x.size(); i++) {
		if ((s == -1) && (x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if ((x[i] == -1) && (s == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if (s > numeric_limits<T>::max() / x[i]) { throw OverflowException(); }  // overflow
		if ((s < numeric_limits<T>::lowest() / x[i])) { throw UnderflowException(); }  // underflow

		p1[i] = x[i] * s;
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < x.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}


/** / operator method **/
/* Element-wise division */
template <typename T>
inline PointND<T> PointND<T>::operator/(PointND<T>& p) {
	assert(x.size() == p.size());  // Check whether 2 points have the same dimensions
	
	vector<T> p1(p.size());  // initialize vector to store answer

	/* Check whether the divisor is equal to zero or not then compute the result */
	for (int i = 0; i < p.size(); i++) {
		if (p.x[i] == 0) { throw DivideByZeroException(); }

		p1[i] = x[i] * (1 / p.x[i]);
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* Scalar division */
template <typename T>
inline PointND<T> PointND<T>::operator/(T s) {
	if (s == 0) { throw DivideByZeroException(); }  // Check whether the divisor is equal to zero or not then compute the result

	vector<T> p1(x.size());  // initialize vector to store answer

	/* Compute the result */
	for (int i = 0; i < x.size(); i++) {
		p1[i] = x[i] / s;
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < x.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}


template <typename T>
void PointND<T>::print(ofstream& f) {
	assert(f);
	f << "(";
	for (int i = 0; i < x.size(); i++) {
		f << x[i];
		if (i < x.size() - 1) {
			f << ", ";
		}
	}
	f << ")";
}

template <typename T>
void PointND<T>::print() {
	cout << "(";
	for (int i = 0; i < x.size(); i++) {
		cout << x[i];
		if (i < x.size() - 1) {
			cout << ", ";
		}
	}
	cout << ")";
}

template class PointND<int>;
template class PointND<float>;
template class PointND<double>;