/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point3D.h"

template <typename T>
class Point4D : public Point3D {
private:
	double z4;
public:
	Point4D(double x, double y, double z, double z4) : Point3D(x, y, z) {
		this->z4 = z4;
	}

	/* + operator method */
	Point4D<T> operator+(Point4D<T> p) {
		return Point4D<T>(getX() + p.getX(), getY() + p.getY(), getZ() + p.getZ(), z4 + p.z4);
	}

	/* - operator method */
	Point4D<T> operator-(Point4D<T> p) {
		return Point4D<T>(getX() - p.getX(), getY() - p.getY(), getZ() - p.getZ(), z4 - p.z4);
	}

	/* * operator method */
	Point4D<T> operator*(double scale) {
		return Point4D<T>(getX() * scale, getY() * scale, getZ() * scale, z4 * scale);
	}

	/* / operator method */
	Point4D<T> operator/(double scale) {
		return Point4D<T>(getX() / scale, getY() / scale, getZ() / scale, z4 / scale);
	}


	void print(ofstream& f);
	void print();
};

