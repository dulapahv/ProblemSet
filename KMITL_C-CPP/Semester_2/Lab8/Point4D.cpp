/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point4D.h"

void Point4D::print(ofstream& f) {
	f << '(' << getX() << ',' << getY() << ',' << z4 << ')';
}
void Point4D::print() {
	cout << '(' << getX() << ', ' << getY() << ', ' << z4 << ')';
}

