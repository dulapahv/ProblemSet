/** PointND class **/

#include <assert.h>
#include <fstream>
#include <iostream>
#include <vector>
#include "assert.h"
#include "math.h"

using namespace std;

#include "PointND.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"
#include "QuadrantException.h"

const int MAX_INT = 2147483647;
const float MAX_FLOAT = 3.402823466e+38F;
const double MAX_DOUBLE = 1.7976931348623158e+308;

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
PointND<T> PointND<T>::operator+(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	vector<T> p1;
	for (int i = 0; i < nd; i++) {
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
PointND<T> PointND<T>::operator-(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	vector<T> p1;
	for (int i = 0; i < nd; i++) {
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
PointND<T> PointND<T>::operator*(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

	vector<T> p1;
	for (int i = 0; i < nd; i++) {
        if (typeid(T) == typeid(int)) {
            if ((x[i] > 0) && (p.x[i] > 0) && (x[i] > MAX_INT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] < 0) && (x[i] < MAX_INT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] > 0) && (p.x[i] < 0) && (x[i] < MAX_INT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] > 0) && (x[i] < MAX_INT / p.x[i])) { throw OverflowException(); }
        }
        else if (typeid(T) == typeid(float)) {
            if ((x[i] > 0) && (p.x[i] > 0) && (x[i] > MAX_FLOAT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] < 0) && (x[i] < MAX_FLOAT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] > 0) && (p.x[i] < 0) && (x[i] < MAX_FLOAT / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] > 0) && (x[i] < MAX_FLOAT / p.x[i])) { throw OverflowException(); }
        }
        else if (typeid(T) == typeid(double)) {
            if ((x[i] > 0) && (p.x[i] > 0) && (x[i] > MAX_DOUBLE / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] < 0) && (x[i] < MAX_DOUBLE / p.x[i])) { throw OverflowException(); }
            else if ((x[i] > 0) && (p.x[i] < 0) && (x[i] < MAX_DOUBLE / p.x[i])) { throw OverflowException(); }
            else if ((x[i] < 0) && (p.x[i] > 0) && (x[i] < MAX_DOUBLE / p.x[i])) { throw OverflowException(); }
        }
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
PointND<T> PointND<T>::operator/(PointND<T>& p) {
    /* Check whether 2 points have the same dimensions */
	assert(nd == p.nd);

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