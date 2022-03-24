/** Point4D class **/

#include <iostream>
#include "math.h"
#include "Point4D.h"
#include "DivideByZeroException.h"
#include "OverflowException.h"

using namespace std;

const int MAX_INT = 2147483647;
const float MAX_FLOAT = 3.402823466e+38F;
const double MAX_DOUBLE = 1.7976931348623158e+308;

template <typename T>
void Point4D<T>::print(ofstream& f) {
	f << "(" << getX() << ", " << getY() << ", " << z4 << ")";
}

template <typename T>
void Point4D<T>::print() {
	cout << "(" << getX() << ", " << getY() << ", " << getZ() << ", " << z4 << ")";
}

/* + operator method */
template <typename T>
Point4D<T> Point4D<T>::operator+(Point4D<T>& p) {
	return Point4D<T>(getX() + p.getX(), getY() + p.getY(), getZ() + p.getZ(), z4 + p.getZ());
}

/* - operator method */
template <typename T>
Point4D<T> Point4D<T>::operator-(Point4D<T>& p) {
	return Point4D<T>(getX() - p.getX(), getY() - p.getY(), getZ() - p.getZ(), z4 - p.getZ());
}

/* * operator method */
template <typename T>
Point4D<T> Point4D<T>::operator*(Point4D<T>& p) {
	if (typeid(T) == typeid(int)) {
		if ((getX() * p.getX() > MAX_INT) || (getY() * p.getY() > MAX_INT) || (getZ() * p.getZ() > MAX_INT) || (z4 * p.getZ() > MAX_INT)) {
			throw OverflowException();
		}
	}
	else if (typeid(T) == typeid(float)) {
		if ((getX() * p.getX() > MAX_FLOAT) || (getY() * p.getY() > MAX_FLOAT) || (getZ() * p.getZ() > MAX_FLOAT) || (z4 * p.getZ() > MAX_FLOAT)) {
			throw OverflowException();
		}
	}
	else {
		if ((getX() * p.getX() > MAX_DOUBLE) || (getY() * p.getY() > MAX_DOUBLE) || (getZ() * p.getZ() > MAX_DOUBLE) || (z4 * p.getZ() > MAX_DOUBLE)) {
			throw OverflowException();
		}
	}

	return Point4D<T>(getX() * p.getX(), getY() * p.getY(), getZ() * p.getZ(), z4 * p.getZ());
}

/* / operator method */
template <typename T>
Point4D<T> Point4D<T>::operator/(Point4D<T>& p) {
	if (p.getX() == 0 || p.getY() == 0 || p.getZ() == 0 || z4 == 0) { throw DivideByZeroException(); }

	return Point4D<T>(getX() / p.getX(), getY() / p.getY(), getZ() / p.getZ(), z4 / p.getZ());
}

template class Point4D<int>;
template class Point4D<float>;
template class Point4D<double>;