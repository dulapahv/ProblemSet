/*** Specification for Rectangle class **/

#include <fstream> 

#include "Point.h"

class Rectangle {
private:
	Point tl, br;
public:
	/** Basic constructors **/
	Rectangle(Point a, Point b);
	Rectangle(float tl[2], float br[2]);
	Rectangle(float xa, float ya, float xb, float yb);

	/** Constructors using an existing template rectangle **/
	/* Make larger version of existing rectangle */
	Rectangle(Rectangle* original, float scale = 1.0f);
	/* Copy existing rectangle, rotate and scale */
	Rectangle(Rectangle* original, float rot = 0.0, float scale = 1.0f);

	Point getTL();
	Point getBR();

	float getArea();
	float getPerimeter();

	void move(float dx, float dy);
	void move(Point dx);
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
	float w = template->br.x – template->tl.x;
	float h = template->br.y – template->tl.y;
	br.x = tl.x + w * scale;
	br.y = tl.y + h * scale;
}
#endif