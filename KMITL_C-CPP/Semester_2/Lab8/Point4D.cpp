/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point4D.h"

template <typename T>
void Point4D<T>::print(ofstream& f) {
	f << '(' << getX() << ',' << getY() << ',' << z4 << ')';
}

template <typename T>
void Point4D<T>::print() {
	cout << '(' << getX() << ', ' << getY() << ', ' << z4 << ')';
}

template class Point4D<int>;
template class Point4D<float>;
template class Point4D<double>;
