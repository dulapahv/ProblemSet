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

template <typename T>
int PointND<T>::XLIMIT = 50;

template <typename T>
int PointND<T>::YLIMIT = 50;

template <typename T>
void PointND<T>::print(ofstream& f) {
	assert(f);
	f << "(";
	for (int i = 0; i < nd; i++) {
		f << x[i];
		if (i < nd - 1) {
			f << ", ";
		}
	}
	f << ")";
}

template <typename T>
void PointND<T>::print() {
	cout << "(";
	for (int i = 0; i < nd; i++) {
		cout << x[i];
		if (i < nd - 1) {
			cout << ", ";
		}
	}
	cout << ")";
}

/* + operator method */
template <typename T>
inline PointND<T> PointND<T>::operator+(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	/* Check for overflow of given data type. If it does not overflow, compute the result */
	vector<T> p1;
	for (int i = 0; i < nd; i++) {
		if ((p.x[i] > 0) && (x[i] > numeric_limits<T>::max() - p.x[i])) { throw OverflowException(); }
		if ((p.x[i] < 0) && (x[i] < numeric_limits<T>::lowest() - p.x[i])) { throw OverflowException(); }

		p1.push_back(x[i] + p.x[i]);
	}

	/* check whether 2 points lie in the first quadrant and inside the limit */
	if (nd == 2) {
		if (!((p1[0] >= 0) && (p1[1] >= 0) && (p1[0] <= XLIMIT) && (p1[1] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* - operator method */
template <typename T>
inline PointND<T> PointND<T>::operator-(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	/* Check for overflow of given data type. If it does not overflow, compute the result */
	vector<T> p1;
	for (int i = 0; i < nd; i++) {
		if ((p.x[i] < 0) && (x[i] > numeric_limits<T>::max() + p.x[i])) { throw OverflowException(); }
		if ((p.x[i] > 0) && (x[i] < numeric_limits<T>::lowest() + p.x[i])) { throw OverflowException(); }

		p1.push_back(x[i] - p.x[i]);
	}

	/* check whether 2 points lie in the first quadrant and inside the limit */
	if (nd == 2) {
		if (!((p1[0] >= 0) && (p1[1] >= 0) && (p1[0] <= XLIMIT) && (p1[1] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* * operator method */
template <typename T>
inline PointND<T> PointND<T>::operator*(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	/* Check for overflow of given data type. If it does not overflow, compute the result */
	vector<T> p1;
	for (int i = 0; i < nd; i++) {
		if ((x[i] == -1) && (x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }
		if ((x[i] == -1) && (p.x[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }
		if (p.x[i] > numeric_limits<T>::max() / x[i]) { throw OverflowException(); }
		if ((p.x[i] < numeric_limits<T>::lowest() / x[i])) { throw OverflowException(); }

		p1.push_back(x[i] * p.x[i]);
	}

	/* check whether 2 points lie in the first quadrant and inside the limit */
	if (nd == 2) {
		if (!((p1[0] >= 0) && (p1[1] >= 0) && (p1[0] <= XLIMIT) && (p1[1] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

/* / operator method */
template <typename T>
inline PointND<T> PointND<T>::operator/(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	/* Check whether the divisor is equal to zero or not. If so, throw DivideByZeroException */
	vector<T> p1;
	for (int i = 0; i < nd; i++) {
		if (p.x[i] == 0) { throw DivideByZeroException(); }

		p1.push_back(x[i] / p.x[i]);
	}

	/* Check whether 2 points lie in the first quadrant and inside the limit */
	if (nd == 2) {
		if (!((p1[0] >= 0) && (p1[1] >= 0) && (p1[0] <= XLIMIT) && (p1[1] <= YLIMIT))) { throw QuadrantException(); }
	}

	return PointND(p1);
}

template class PointND<int>;
template class PointND<float>;
template class PointND<double>;