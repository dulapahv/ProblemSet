/** Point4D class **/

#include <iostream>
#include <limits>
#include "assert.h"
#include "math.h"

using namespace std;

#include "Point4D.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"
#include "UnderflowException.h"

template <typename T>
void Point4D<T>::print(ofstream& f) {
	assert(f);
	f << "(" << getX() << ", " << getY() << ", " << getZ() << ", " << z4 << ")";
}

template <typename T>
void Point4D<T>::print() {
	cout << "(" << getX() << ", " << getY() << ", " << getZ() << ", " << z4 << ")";
}

/** + operator method **/
/* Element-wise addition */
template <typename T>
inline Point4D<T> Point4D<T>::operator+(Point4D<T>& p) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	T pChk[4] = { p.getX(), p.getY(), p.getZ(), p.z4 };
	for (int i = 0; i < 4; i++) {
		if ((pChk[i] > 0) && (chk[i]) > numeric_limits<T>::max() - pChk[i]) { throw OverflowException(); }  // overflow
		if ((pChk[i] < 0) && (chk[i]) < numeric_limits<T>::lowest() - pChk[i]) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() + p.getX(), getY() + p.getY(), getZ() + p.getZ(), z4 + p.z4);
}

/* Scalar addition */
template <typename T>
inline Point4D<T> Point4D<T>::operator+(T s) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	for (int i = 0; i < 4; i++) {
		if ((s > 0) && (chk[i] > numeric_limits<T>::max() - s)) { throw OverflowException(); }  // overflow
		if ((s < 0) && (chk[i] < numeric_limits<T>::lowest() - s)) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() + s, getY() + s, getZ() + s, z4 + s);
}


/** - operator method **/
/* Element-wise subtraction */
template <typename T>
inline Point4D<T> Point4D<T>::operator-(Point4D<T>& p) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	T pChk[4] = { p.getX(), p.getY(), p.getZ(), p.z4 };
	for (int i = 0; i < 4; i++) {
		if ((pChk[i] < 0) && (chk[i]) > numeric_limits<T>::max() + pChk[i]) { throw OverflowException(); }  // overflow
		if ((pChk[i] > 0) && (chk[i]) < numeric_limits<T>::lowest() + pChk[i]) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() - p.getX(), getY() - p.getY(), getZ() - p.getZ(), z4 - p.z4);
}

/* Scalar subtraction */
template <typename T>
inline Point4D<T> Point4D<T>::operator-(T s) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	for (int i = 0; i < 4; i++) {
		if ((s < 0) && (chk[i] > numeric_limits<T>::max() + s)) { throw OverflowException(); }  // overflow
		if ((s > 0) && (chk[i] < numeric_limits<T>::lowest() + s)) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() - s, getY() - s, getZ() - s, z4 - s);
}


/** * operator method **/
/* Element-wise multiplication */
template <typename T>
inline Point4D<T> Point4D<T>::operator*(Point4D<T>& p) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	T pChk[4] = { p.getX(), p.getY(), p.getZ(), p.z4 };
	for (int i = 0; i < 4; i++) {
		if ((pChk[i] == -1) && (chk[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if ((chk[i] == -1) && (pChk[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if (pChk[i] > numeric_limits<T>::max() / chk[i]) { throw OverflowException(); }  // overflow
		if ((pChk[i] < numeric_limits<T>::lowest() / chk[i])) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() * p.getX(), getY() * p.getY(), getZ() * p.getZ(), z4 * p.z4);
}

/* Scalar multiplication */
template <typename T>
inline Point4D<T> Point4D<T>::operator*(T s) {
	/* Check for overflow of given data type then compute the result */
	T chk[4] = { getX(), getY(), getZ(), z4 };
	for (int i = 0; i < 4; i++) {
		if ((s == -1) && (chk[i] == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if ((chk[i] == -1) && (s == numeric_limits<T>::lowest())) { throw OverflowException(); }  // overflow
		if (s > numeric_limits<T>::max() / chk[i]) { throw OverflowException(); }  // overflow
		if ((s < numeric_limits<T>::lowest() / chk[i])) { throw UnderflowException(); }  // underflow
	}

	return Point4D<T>(getX() * s, getY() * s, getZ() * s, z4 * s);
}


/** / operator method **/
/* Element-wise division */
template <typename T>
inline Point4D<T> Point4D<T>::operator/(Point4D<T>& p) {
	/* Check for overflow of given data type then compute the result */
	if ((p.getX() == 0) || (p.getY() == 0) || (p.getZ() == 0) || (z4 == 0)) { throw DivideByZeroException(); }

	return Point4D<T>(getX() * (1 / p.getX()), getY() * (1 / p.getY()), getZ() * (1 / p.getZ()), z4 * (1 / p.z4));
}

/* Scalar division */
template <typename T>
inline Point4D<T> Point4D<T>::operator/(T s) {
	/* Check for overflow of given data type then compute the result */
	if (s == 0) { throw DivideByZeroException(); }

	return Point4D<T>(getX() / s, getY() / s, getZ() / s, z4 / s);
}

template class Point4D<int>;
template class Point4D<float>;
template class Point4D<double>;