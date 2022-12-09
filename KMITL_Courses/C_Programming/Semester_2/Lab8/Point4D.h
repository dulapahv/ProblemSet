/** Point4D class **/

#pragma once

#include <iostream>
#include "math.h"

using namespace std;

#include "Point3D.h"

template <typename T>
class Point4D : public Point3D {
private:
	T z4;
public:
	Point4D(T x, T y, T z, T z4) : Point3D(x, y, z) {
		this->z4 = z4;
	}

	/* + operator method */
	Point4D<T> operator+(Point4D<T>& p); // Element-wise addition
	Point4D<T> operator+(T a); // Scalar addition

	/* - operator method */
	Point4D<T> operator-(Point4D<T>& p); // Element-wise subtraction
	Point4D<T> operator-(T a); // Scalar subtraction

	/* * operator method */
	Point4D<T> operator*(Point4D<T>& p); // Element-wise multiplication
	Point4D<T> operator*(T a); // Scalar multiplication

	/* / operator method */
	Point4D<T> operator/(Point4D<T>& p); // Element-wise division
	Point4D<T> operator/(T a); // Scalar division

	void print(ofstream& f);
	void print();
};
