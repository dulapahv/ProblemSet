/** Point3D class **/

#include <iostream>
#include "math.h"
#include "Point4D.h"
#include "DivideByZeroException.h"
#include "OverflowException.h"

using namespace std;

template <typename T>
void Point4D<T>::print(ofstream& f) {
	f << '(' << getX() << ',' << getY() << ',' << z4 << ')';
}

template <typename T>
void Point4D<T>::print() {
	cout << '(' << getX() << ', ' << getY() << ', ' << z4 << ')';
}

/* + operator method */
template <typename T>
Point4D<T> operator+(Point4D<T> p, T scale) {
	if (p.getX() + scale > numeric_limits<T>::max() || p.getX() + scale < numeric_limits<T>::min()) {
		throw OverflowException();
	}
	return Point4D<T>(p.getX() + scale, p.getY() + scale, p.getZ() + scale, p.z4 + scale);
}

template <typename T>
Point4D<T> operator+(Point4D<T> p1, Point4D<T> p2) {
	if (p1.getX() + p2.getX() > numeric_limits<T>::max() || p1.getX() + p2.getX() < numeric_limits<T>::min()) {
		throw OverflowException();
	}
	return Point4D<T>(p1.getX() + p2.getX(), p1.getY() + p2.getY(), p1.getZ() + p2.getZ(), p1.z4 + p2.z4);
}

/* - operator method */
template <typename T>
Point4D<T> operator-(Point4D<T> p, T scale) {
	if (p.getX() - scale > numeric_limits<T>::max() || p.getX() - scale < numeric_limits<T>::min()) {
		throw OverflowException();
	}
	return Point4D<T>(p.getX() - scale, p.getY() - scale, p.getZ() - scale, p.z4 - scale);
}

template <typename T>
Point4D<T> operator-(Point4D<T> p1, Point4D<T> p2) {
	if (p1.getX() - p2.getX() > numeric_limits<T>::max() || p1.getX() - p2.getX() < numeric_limits<T>::min()) {
		throw OverflowException();
	}
	return Point4D<T>(p1.getX() - p2.getX(), p1.getY() - p2.getY(), p1.getZ() - p2.getZ(), p1.z4 - p2.z4);
}

/* * operator method */
template <typename T>
Point4D<T> operator*(Point4D<T> p, T scale) {
	if ((p.getX() > 0) && (p.getX() * scale > numeric_limits<T>::max())) {
		throw OverflowException();
	}
	else if ((p.getX() < 0) && (p.getX() * scale < numeric_limits<T>::min())) {
		throw OverflowException();
	}
	return Point4D<T>(p.getX() * scale, p.getY() * scale, p.getZ() * scale, p.z4 * scale);
}

template <typename T>
Point4D<T> operator*(Point4D<T> p1, Point4D<T> p2) {
	if ((p1.getX() > 0) && (p1.getX() * p2.getX() > numeric_limits<T>::max())) {
		throw OverflowException();
	}
	else if ((p1.getX() < 0) && (p1.getX() * p2.getX() < numeric_limits<T>::min())) {
		throw OverflowException();
	}
	return Point4D<T>(p1.getX() * p2.getX(), p1.getY() * p2.getY(), p1.getZ() * p2.getZ(), p1.z4 * p2.z4);
}

/* / operator method */
template <typename T>
Point4D<T> operator/(Point4D<T> p, T scale) {
	if (scale == 0) {
		throw DivideByZeroException();
	}
	return Point4D<T>(p.getX() / scale, p.getY() / scale, p.getZ() / scale, p.z4 / scale);
}

template <typename T>
Point4D<T> operator/(Point4D<T> p1, Point4D<T> p2) {
	if ((p2.getX() == 0) || (p2.getY() == 0) || (p2.getZ() == 0) || (p2.z4 == 0)) {
		throw DivideByZeroException();
	}
	return Point4D<T>(p1.getX() / p2.getX(), p1.getY() / p2.getY(), p1.getZ() / p2.getZ(), p1.z4 / p2.z4);
}

template class Point4D<int>;
template class Point4D<float>;
template class Point4D<double>;

/* / operator method */
// template <typename T>
// Point4D<T> operator/(Point4D<T> p, T scale) {
// 	if (scale == 0) {
// 		throw DivideByZeroException();
// 	}
// 	return Point4D<T>(p.getX() / scale, p.getY() / scale, p.getZ() / scale, p.z4 / scale);
// }

// template <typename T>
// Point4D<T> operator/(Point4D<T> p1, Point4D<T> p2) {
// 	if ((p2.getX() == 0) || (p2.getY() == 0) || (p2.getZ() == 0) || (p2.z4 == 0)) {
// 		throw DivideByZeroException();
// 	}
// 	return Point4D<T>(p1.getX() / p2.getX(), p1.getY() / p2.getY(), p1.getZ() / p2.getZ(), p1.z4 / p2.z4);
// }

