/** Implementation of the Rectangle class **/

#include <ctype.h>
#include "assert.h"
#include "Rectangle.h"

Rectangle::Rectangle(Point a, Point b) {
	tl = a; br = b;
}

Rectangle::Rectangle(float tlx[2], float brx[2]) {
	tl.x = tlx[0]; tl.y = tlx[1];
	br.x = brx[0]; br.y = brx[1];
}

Rectangle::Rectangle(float xa, float ya, float xb, float yb) {
	tl = Point(xa, ya);
	br = Point(xb, yb);
}

/* Make larger version of existing rectangle */
Rectangle::Rectangle(Rectangle* orig, float scale) {
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

Point Rectangle::getTL() { return tl; }
Point Rectangle::getBR() { return br; }

float Rectangle::getArea() {
	float w = br.x - tl.x;
	float h = br.y - tl.y;
	return w * h;
}
float Rectangle::getPerimeter() {
	float w = br.x - tl.x;
	float h = br.y = tl.y;
	return 2.0f * (w + h);
}

void Rectangle::move(float dx, float dy) {
	tl.x = tl.x + dx; br.x = br.x + dy;
	tl.y = tl.y + dy; br.y = br.y + dy;
}

void Rectangle::move(Point dx) {
	tl.x = tl.x + dx.x; br.x = br.x + dx.y;
	tl.y = tl.y + dx.x; br.y = br.y + dx.y;
}

Point nextGridPoint(Rectangle& r) {
	Point dx(1.0, 1.0);
	r.move(dx);
	return r.getTL();
}

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