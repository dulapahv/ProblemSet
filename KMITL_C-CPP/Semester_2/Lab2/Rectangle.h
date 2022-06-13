/*** Specification for Rectangle class **/

#pragma once

#include <fstream> 

#include "Pt.h"

using namespace std;

template <typename T>
class Rect {
private:
	Pt<T> tl, br;
public:
	/** Basic constructors **/
	Rect(Pt<T> a, Pt<T> b);
	Rect(T tl[2], T br[2]);
	Rect(T xa, T ya, T xb, T yb);

	/** Constructors using an existing template rectangle **/
	/* Make larger version of existing rectangle */
	Rect(Rect* original, float scale = 1.0f);
	/* Copy existing rectangle, rotate and scale */
	Rect(Rect* original, float rot = 0.0, float scale = 1.0f);

	Pt<T> getTL();
	Pt<T> getBR();

	float getArea();
	float getPerimeter();

	void move(float dx, float dy);
	void move(Pt<T> dx);

	void print();
};

#ifdef OLD
Rectangle::Rectangle(Point a, Point b) {
	tl = a; br = b;
}
Rectangle::Rectangle(float tl[2], float br[2]) {
	tl.x = tl[0]; tl.y = tl[1];
	br.x = br[0]; br.y = br[1];
}
/* Make larger version of existing rectangle */
Rectangle::Rectangle(Rectangle* original, float scale = 1.0f) {
	tl = template.tl;
	float w = template->br.x � template->tl.x;
	float h = template->br.y � template->tl.y;
	br.x = tl.x + w * scale;
	br.y = tl.y + h * scale;
}
#endif