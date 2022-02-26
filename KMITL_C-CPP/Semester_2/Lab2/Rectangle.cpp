/** Implementation of the Rectangle class **/

#include <ctype.h>
#include <math.h>
#include <iostream>
#include "assert.h"
#include "Rectangle.h"

template <typename T>
Rect<T>::Rect(Pt<T> a, Pt<T> b) {
	tl = a; br = b;
}

template <typename T>
Rect<T>::Rect(T tlx[2], T brx[2]) {
	tl.x = tlx[0]; tl.y = tlx[1];
	br.x = brx[0]; br.y = brx[1];
}

template <typename T>
Rect<T>::Rect(T xa, T ya, T xb, T yb) {
	tl = Pt<T>(xa, ya);
	br = Pt<T>(xb, yb);
}

/* Make larger version of existing rectangle */
template <typename T>
Rect<T>::Rect(Rect* orig, float scale) {
	assert(orig != NULL);
	assert(orig->getArea() > 0.0f);
	assert(!isnan(scale));
	assert(scale > 0.0f);
	tl = orig->tl;
	float w = orig->br.x - orig->tl.x;
	float h = orig->br.y - orig->tl.y;
	br.x = tl.x + w * scale;
	br.y = tl.y + h * scale;
}

template <typename T>
Rect<T>::Rect(Rect* orig, float rot, float scale) {
	assert(orig != NULL);
	assert(orig->getArea() > 0.0f);
	assert(!isnan(scale));
	assert(scale > 0.0f);
	tl = orig->tl;
	float w = orig->br.x - orig->tl.x;
	float h = orig->br.y - orig->tl.y;
	br.x = tl.x + w * scale;
	br.y = tl.y + h * scale;
}

template <typename T>
Pt<T> Rect<T>::getTL() { return tl; }

template <typename T>
Pt<T> Rect<T>::getBR() { return br; }

template <typename T>
float Rect<T>::getArea() {
	float w = br.x - tl.x;
	float h = br.y - tl.y;
	return w * h;
}

template <typename T>
float Rect<T>::getPerimeter() {
	float w = br.x - tl.x;
	float h = br.y = tl.y;
	return 2.0f * (w + h);
}

template <typename T>
void Rect<T>::move(float dx, float dy) {
	tl.x = tl.x + dx; br.x = br.x + dy;
	tl.y = tl.y + dy; br.y = br.y + dy;
}

template <typename T>
void Rect<T>::move(Pt<T> dx) {
	tl.x = tl.x + dx.x; br.x = br.x + dx.y;
	tl.y = tl.y + dx.x; br.y = br.y + dx.y;
}

template <typename T>
Pt<T> nextGridPoint(Rect<T>& r) {
	Pt<T> dx(1.0, 1.0);
	r.move(dx);
	return r.getTL();
}

template <typename T>
void Rect<T>::print() {
	Pt<T> pt1, pt2;
	pt1 = getTL();
	pt2 = getBR();
	cout << "TL: (" << pt1.getX() << ", " << pt1.getY() << ") BR: (" << pt2.getX() << ", " << pt2.getY() << ")" << endl;
}

template class Rect<int>;
template class Rect<float>;
template class Rect<double>;

#ifdef OLD
Point getNextGridPoint(const Rectangle& r) {
	Point dx(1.0, 1.0);
	// r.move(dx);
	// return r.getTL();
	Point next_pt = r.getTL();
	next_pt.x += dx.x; next_pt.y += dx.y;
	return next_pt;
}
#endif