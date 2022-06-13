#include <iostream>
#include <vector>
#include "Rectangle.h"

#define N_LARGE 1000

using namespace std;

int main() {
	/* a) Create a small (or default) vector. Check its allocated space with v.capacity(); */
	vector<Rect<double>> rectVector;
	rectVector.reserve(N_LARGE);
	cout << "Space reserved for rectangle vector: " << rectVector.capacity() << endl;

	/* b) Add more elements in a loop with push_back() */
	int add = 20;
	cout << "Rectangles added: " << add <<endl;
	for (int i = 0; i < add; i++) {
		Rect<double> *rect = new Rect<double>(1.2 * i, 1.4 * i, 2.6 * i, 2.8 * i);
		rectVector.push_back(*rect);
		rect->print();
	}
	cout << "\nAll rectangles in rectangle vector: " << rectVector.size() << endl;
	for (auto i = rectVector.begin(); i != rectVector.end(); i++) {
		i->print();
	}

	/* c) Use capacity() to see how many more where added */
	vector<int> a;
	cout << "\nSpace allocated for vector a: " << a.capacity() << endl;
	for (int i = 0; i < 1000; i++) {
		a.push_back(i);
	}
	cout << "Space of vector a after adding 1000 integers: " << a.capacity() << endl;

	/* d) Use the reserve(new_capacity) */
	vector<int> b;
	b.reserve(1000);
	cout << "\nSpace reserved for vector b: " << b.capacity() << endl;
	for (int i = 0; i < 1000; i++) {
		b.push_back(i);
	}
	cout << "Space of vector b after adding 1000 integers: " << b.capacity() << endl;

	return 0;
}