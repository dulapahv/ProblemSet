#include <iostream>
#include <vector>
#include "Point4D.h"
#include "PointND.h"
#include "OverflowException.h"
#include "DivideByZeroException.h"
#include "QuadrantException.h"

using namespace std;

int main() {
	/** Testing Point4D Class **/
	Point4D<int> setInt1(1, 2, 3, 4);
	Point4D<int> setInt2(5, 6, 7, 8);
	Point4D<int> setIntLimit(2147483647, 2147483647, 2147483647, 2147483647);
	Point4D<float> setFloat1(1.87, 2.65, 3.43, 4.21);
	Point4D<float> setFloat2(5.21, 6.43, 7.65, 8.87);
	Point4D<double> setDouble1(1.21, 2.43, 3.65, 4.87);
	Point4D<double> setDouble2(5.87, 6.65, 7.43, 8.21);
	Point4D<double> setZero(0, 0, 0, 0);

	/* Test + operator method */
	Point4D<int> Sum = setInt1 + setInt2;
	setInt1.print(); cout << " + "; setInt2.print(); cout << " = "; Sum.print(); cout << endl;

	/* Test - operator method */
	Point4D<float> Diff = setFloat1 - setFloat2;
	setFloat1.print(); cout << " - "; setFloat2.print(); cout << " = "; Diff.print(); cout << endl;

	/* Test * operator method */
	Point4D<double> Prod = setDouble1 * setDouble2;
	setDouble1.print(); cout << " * "; setDouble2.print(); cout << " = "; Prod.print(); cout << endl;

	/* Test / operator method */
	Point4D<double> Quot = setDouble1 / setDouble2;
	setDouble1.print(); cout << " / "; setDouble2.print(); cout << " = "; Quot.print(); cout << endl;

	/* Test DivideByZeroException */
	setDouble1.print(); cout << " / "; setZero.print(); cout << " = ";
	try {
		Point4D<double> testQuot = setDouble1 / setZero;
		testQuot.print();
	}
	catch (DivideByZeroException e) {
		cout << e.what();
	}

	/* Test OverflowException */
	setInt1.print(); cout << " * "; setIntLimit.print(); cout << " = ";
	try {
		Point4D<int> testProd = setInt1 * setIntLimit;
		testProd.print();
	}
	catch (OverflowException e) {
		cout << e.what();
	}


	/** Testing PointND Class **/
	PointND<int> setInt3(vector<int>{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
	PointND<int> setInt4(vector<int>{ 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 });
	PointND<int> setIntLimit2(vector<int>{ 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647 });
	PointND<float> setFloat3(vector<float> { 1.87, 2.65, 3.43, 4.21, 5.01, 6.11, 7.21, 8.31, 9.41, 10.51 });
	PointND<float> setFloat4(vector<float> { 5.21, 6.43, 7.65, 8.87, 9.99, 10.11, 11.23, 12.35, 13.47, 14.59 });
	PointND<double> setDouble3(vector<double> { 1.21, 2.43, 3.65, 4.87, 5.99, 6.11, 7.23, 8.35, 9.47, 10.59 });
	PointND<double> setDouble4(vector<double> { 5.87, 6.65, 7.43, 8.21, 9.01, 10.11, 11.21, 12.31, 13.41, 14.51 });
	PointND<double> setZero2(vector<double> (10, 0));

	/* Test + operator method */
	PointND<int> Sum2 = setInt3 + setInt4;
	//(setInt3 + setInt4).print()
	Sum2.print();
	cout << endl;

	/* Test - operator method */
	PointND<float> Diff2 = setFloat3 - setFloat4;
	Diff2.print();
	cout << endl;

	/* Test * operator method */
	PointND<double> Prod2 = setDouble3 * setDouble4;
	Prod2.print();
	cout << endl;

	/* Test / operator method */
	PointND<double> Quot2 = setDouble3 / setDouble4;
	Quot2.print();
	cout << endl;


	/** Test DivideByZeroException **/
	try {
		PointND<double> testQuot2 = setDouble3 / setZero2;
		testQuot2.print();
	}
	catch (DivideByZeroException e) {
		cout << e.what();
	}
	

	/** Test OverflowException **/
	try {
		PointND<int> testProd2 = setInt3 * setIntLimit2;
		testProd2.print();
	}
	catch (OverflowException e) {
		cout << e.what();
	}


	/** Testing QuadrantException Class **/
	// XLIMIT = 50, YLIMIT = 50
	PointND<int> pt1(vector<int> { 12, 2 });
	PointND<int> pt2(vector<int> { 5, 8 });

	/* In the first quadrant */
	try {
		PointND<int> ptAns1 = pt1 + pt2;
	}
	catch (QuadrantException e) {
		cout << e.what();
	}

	/* Not in the first quadrant */
	try {
		PointND<int> ptAns2 = pt1 - pt2;
	}
	catch (QuadrantException e) {
		cout << e.what();
	}

	/* Exceeding the limit in the first quadrant */
	try {
		PointND<int> ptAns3 = pt1 * pt2;
	}
	catch (QuadrantException e) {
		cout << e.what();
	}

	return 0;
}