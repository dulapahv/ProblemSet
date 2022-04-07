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
	return this->nd;
}

/* + operator method */
template <typename T>
inline PointND<T> PointND<T>::operator+(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(x.size() == p.size());

	vector<T> p1(p.size());
	for (int i = 0; i < p.size(); i++) {
		/* Check for overflow of given data type */
		if ((p.x[i] > 0) && (x[i] > numeric_limits<T>::max() - p.x[i])) { throw OverflowException(); }  // overflow
		if ((p.x[i] < 0) && (x[i] < numeric_limits<T>::lowest() - p.x[i])) { throw UnderflowException(); }  // underflow

		/* Compute the result */
		p1[i] = x[i] + p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* - operator method */
template <typename T>
inline PointND<T> PointND<T>::operator-(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(x.size() == p.size());

	vector<T> p1(p.size());
	for (int i = 0; i < p.size(); i++) {
		/* Check for overflow of given data type */
		if ((p.x[i] < 0) && (x[i] > numeric_limits<T>::max() + p.x[i])) { throw OverflowException(); }  // overflow
		if ((p.x[i] > 0) && (x[i] < numeric_limits<T>::lowest() + p.x[i])) { throw UnderflowException(); }  // underflow

		/* Compute the result */
		p1[i] = x[i] - p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* * operator method */
template <typename T>
inline PointND<T> PointND<T>::operator*(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(x.size() == p.size());

	vector<T> p1(p.size());
	/* Check for overflow of given data type */
	for (int i = 0; i < p.size(); i++) {
		if ((p.x[i] == -1) && (x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if ((x[i] == -1) && (p.x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if (p.x[i] > numeric_limits<T>::max() / x[i]) { throw OverflowException(); }  // overflow
		if ((p.x[i] < numeric_limits<T>::lowest() / x[i])) { throw UnderflowException(); }  // underflow

		/* Compute the result */
		p1[i] = x[i] * p.x[i];
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
		if (!((p1[i] >= 0) && (p1[i] <= XLIMIT) && (p1[i] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* / operator method */
template <typename T>
inline PointND<T> PointND<T>::operator/(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(x.size() == p.size());

	/* Check whether the divisor is equal to zero or not. If so, throw DivideByZeroException */
	vector<T> p1(p.size());
	for (int i = 0; i < p.size(); i++) {
		/* Check whether the divisor is equal to zero or not */
		if (p.x[i] == 0) { throw DivideByZeroException(); }

		/* Compute the result */
		p1[i] = x[i] * (1 / p.x[i]);
	}

	/* Check whether the point lies in the first quadrant and inside the limit or not */
	for (int i = 0; i < p.size(); i++) {
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