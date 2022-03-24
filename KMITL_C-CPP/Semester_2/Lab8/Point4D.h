/** Point3D class **/

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
	Point4D<T> operator+(T scale);
	Point4D<T> operator+(Point4D<T> p);
	//Point4D<T> operator+(Point4D<T> p1, Point4D<T> p2) { }

	/* - operator method */
	Point4D<T> operator-(T scale);
	Point4D<T> operator-(Point4D<T> p);
	//Point4D<T> operator-(Point4D<T> p1, Point4D<T> p2) { }

	/* * operator method */
	Point4D<T> operator*(Point4D<T> p);
	Point4D<T> operator*(T scale);
	//Point4D<T> operator*(Point4D<T> p1, Point4D<T> p2) { }

	/* / operator method */
	Point4D<T> operator/(Point4D<T> p);
	Point4D<T> operator/(T scale);
	//Point4D<T> operator/(Point4D<T> p1, Point4D<T> p2) { }

	void print(ofstream& f);
	void print();
};
