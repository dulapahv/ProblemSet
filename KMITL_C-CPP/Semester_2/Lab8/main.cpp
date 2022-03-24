#include <iostream>
#include "Point4D.h"

using namespace std;

int main() {
	/* Test + operator method */
	Point4D<int> Add1(1, 2, 3, 4), Add2(5, 6, 7, 8);
	Point4D<int> Sum = Add1 + Add2;
	Sum.print();
	cout << endl;

	/* Test - operator method */
	Point4D<float> Sub1(5.21, 6.43, 7.65, 8.87), Sub2(1.87, 2.65, 3.43, 4.21);
	Point4D<float> Diff = Sub1 - Sub2;
	Diff.print();
	cout << endl;

	/* Test * operator method */
	Point4D<double> Mult1(1.21, 2.43, 3.65, 4.87), Mult2(5.87, 6.65, 7.43, 8.21);
	Point4D<double> Prod = Mult1 * Mult2;
	Prod.print();
	cout << endl;

	/* Test / operator method */
	Point4D<double> Div1(1.21, 2.43, 3.65, 4.87), Div2(5.87, 6.65, 7.43, 8.21);
	Point4D<double> Quot = Div1 / Div2;
	Quot.print();
	cout << endl;

	/* Test DivideByZeroException */
	Point4D<double> testDiv1(1.21, 2.43, 3.65, 4.87), testDiv2(0, 0, 0, 0);
	try {
		Point4D<double> testQuot = testDiv1 / testDiv2;
		testQuot.print();
	}
	catch (DivideByZeroException e) {
		cout << e.what();
	}

	/* Test OverflowException */
	Point4D<int> testMult1(1, 2, 3, 4), testMult2(2147483647, 2147483647, 2147483647, 2147483647);
	try {
		Point4D<int> testProd = testMult1 * testMult2;
		testProd.print();
	}
	catch (OverflowException e) {
		cout << e.what();
	}

	return 0;
}