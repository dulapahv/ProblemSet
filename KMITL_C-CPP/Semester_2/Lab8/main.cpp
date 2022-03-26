#include <fstream>
#include <iostream>
#include <vector>
#include "assert.h"

using namespace std;

#include "Point4D.h"
#include "PointND.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"
#include "QuadrantException.h"

int main() {
	ofstream outFile("output.txt");
	assert(outFile);

	/** Testing Point4D Class **/
	Point4D<int> setInt1(1, 2, 3, 4);
	Point4D<int> setInt2(5, 6, 7, 8);
	Point4D<int> setIntLimit(2147483647, 2147483647, 2147483647, 2147483647);
	Point4D<float> setFloat1(1.87, 2.65, 3.43, 4.21);
	Point4D<float> setFloat2(5.21, 6.43, 7.65, 8.87);
	Point4D<double> setDouble1(1.21, 2.43, 3.65, 4.87);
	Point4D<double> setDouble2(5.87, 6.65, 7.43, 8.21);
	Point4D<double> setZero(0, 0, 0, 0);

	outFile << "==[Testing Point4D Class]===========================================" << endl;
	outFile << "Declared Points" << endl;
	outFile << typeid(setInt1).name() << " setInt1"; setInt1.print(outFile); outFile << endl;
	outFile << typeid(setInt2).name() << " setInt2"; setInt2.print(outFile); outFile << endl;
	outFile << typeid(setIntLimit).name() << " setIntLimit"; setIntLimit.print(outFile); outFile << endl;
	outFile << typeid(setFloat1).name() << " setFloat1"; setFloat1.print(outFile); outFile << endl;
	outFile << typeid(setFloat2).name() << " setFloat2"; setFloat2.print(outFile); outFile << endl;
	outFile << typeid(setDouble1).name() << " setDouble1"; setDouble1.print(outFile); outFile << endl;
	outFile << typeid(setDouble2).name() << " setDouble2"; setDouble2.print(outFile); outFile << endl;
	outFile << typeid(setZero).name() << " setZero"; setZero.print(outFile); outFile << endl;

	outFile << endl;

	/** Testing Operator Methods **/
	outFile << "Testing Operator Methods" << endl;

	/* + operator method */
	Point4D<int> sum = setInt1 + setInt2;
	outFile << "+ operator method: (setInt1 + setInt2) = "; sum.print(outFile); outFile << endl;

	/* - operator method */
	Point4D<float> diff = setFloat1 - setFloat2;
	outFile << "- operator method: (setFloat1 - setFloat2) = "; diff.print(outFile); outFile << endl;

	/* * operator method */
	Point4D<double> prod = setDouble1 * setDouble2;
	outFile << "* operator method: (setDouble1 * setDouble2) = "; prod.print(outFile); outFile << endl;

	/* / operator method */
	Point4D<double> quot = setDouble1 / setDouble2;
	outFile << "/ operator method: (setDouble1 / setDouble2) = "; quot.print(outFile); outFile << endl;

	/* Combining operator methods */
	Point4D<double> mix1 = (((setDouble1 + setDouble2) * setDouble2) - setDouble1) / setDouble2;
	outFile << "Combining operator methods: ((((setDouble1 + setDouble2) * setDouble2) - setDouble1) / setDouble2) = "; mix1.print(outFile); outFile << endl;
	
	outFile << endl;


	/** Testing Exceptions **/
	outFile << "Testing Exceptions" << endl;

	/* Test DivideByZeroException */
	outFile << "Dividing by zero: (setDouble1 / setZero) = ";
	try {
		Point4D<double> testQuot = setDouble1 / setZero;
	}
	catch (DivideByZeroException e) {
		outFile << e.what();
	}

	/* Test OverflowException */
	outFile << "Overflowing a data type: (setInt1 * setIntLimit) = ";
	try {
		Point4D<int> testProd = setInt1 * setIntLimit;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}

	outFile << endl;


	/** Testing PointND Class **/
	PointND<int> setInt3(vector<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
	PointND<int> setInt4(vector<int> { 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 });
	PointND<int> setIntLimit2(vector<int> (10, 2147483647));
	PointND<float> setFloat3(vector<float> { 1.87, 2.65, 3.43, 4.21, 5.01, 6.11, 7.21, 8.31, 9.41, 10.51 });
	PointND<float> setFloat4(vector<float> { 5.21, 6.43, 7.65, 8.87, 9.99, 10.11, 11.23, 12.35, 13.47, 14.59 });
	PointND<double> setDouble3(vector<double> { 1.21, 2.43, 3.65, 4.87, 5.99, 6.11, 7.23, 8.35, 9.47, 10.59 });
	PointND<double> setDouble4(vector<double> { 5.87, 6.65, 7.43, 8.21, 9.01, 10.11, 11.21, 12.31, 13.41, 14.51 });
	PointND<double> setZero2(vector<double> (10, 0));
	PointND<int> pt1(vector<int> { 12, 2 });
	PointND<int> pt2(vector<int> { 5, 8 });

	outFile << "==[Testing PointND Class]===========================================" << endl;
	outFile << "Declared Points" << endl;
	outFile << typeid(setInt3).name() << " setInt3"; setInt3.print(outFile); outFile << endl;
	outFile << typeid(setInt4).name() << " setInt4"; setInt4.print(outFile); outFile << endl;
	outFile << typeid(setIntLimit2).name() << " setIntLimit2"; setIntLimit2.print(outFile); outFile << endl;
	outFile << typeid(setFloat3).name() << " setFloat3"; setFloat3.print(outFile); outFile << endl;
	outFile << typeid(setFloat4).name() << " setFloat4"; setFloat4.print(outFile); outFile << endl;
	outFile << typeid(setDouble3).name() << " setDouble3"; setDouble3.print(outFile); outFile << endl;
	outFile << typeid(setDouble4).name() << " setDouble4"; setDouble4.print(outFile); outFile << endl;
	outFile << typeid(setZero2).name() << " setZero2"; setZero2.print(outFile); outFile << endl;
	outFile << typeid(pt1).name() << " pt1"; pt1.print(outFile); outFile << endl;
	outFile << typeid(pt2).name() << " pt2"; pt2.print(outFile); outFile << endl;

	outFile << endl;

	/** Testing Operator Methods **/
	outFile << "Testing Operator Methods" << endl;

	/* + operator method */
	PointND<int> sum2 = setInt3 + setInt4;
	outFile << "+ operator method: (setInt3 + setInt4) = "; sum2.print(outFile); outFile << endl;

	/* - operator method */
	PointND<float> diff2 = setFloat3 - setFloat4;
	outFile << "- operator method: (setFloat3 - setFloat4) = "; diff2.print(outFile); outFile << endl;

	/* * operator method */
	PointND<double> prod2 = setDouble3 * setDouble4;
	outFile << "* operator method: (setDouble3 * setDouble4) = "; prod2.print(outFile); outFile << endl;

	/* / operator method */
	PointND<double> quot2 = setDouble3 / setDouble4;
	outFile << "/ operator method: (setDouble3 / setDouble4) = "; quot2.print(outFile); outFile << endl;

	/* Combining operator methods */
	PointND<double> mix2 = (((setDouble3 + setDouble4) * setDouble4) - setDouble3) / setDouble4;
	outFile << "Combining operator methods: ((((setDouble3 + setDouble4) * setDouble4) - setDouble3) / setDouble4) = "; mix2.print(outFile); outFile << endl;

	outFile << endl;


	/** Testing Exceptions **/
	outFile << "Testing Exceptions" << endl;

	/* Test DivideByZeroException */
	outFile << "Dividing by zero: (setDouble3 / setZero2) = ";
	try {
		PointND<double> testQuot2 = setDouble3 / setZero2;
	}
	catch (DivideByZeroException e) {
		outFile << e.what();
	}

	/* Test OverflowException */
	outFile << "Overflowing a data type: (setInt3 * setIntLimit2) = ";
	try {
		PointND<int> testProd2 = setInt3 * setIntLimit2;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}

	outFile << endl;


	/** Testing QuadrantException Class **/
	// XLIMIT = 50, YLIMIT = 50
	outFile << "Testing Whether The Point Lies In The First Quadrant Or Not (XLIMIT = 50, YLIMIT = 50)" << endl;

	/* In the first quadrant */
	outFile << "(pt1 + pt2) = ";
	try {
		PointND<int> ptAns1 = pt1 + pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}

	/* Not in the first quadrant */
	outFile << "(pt1 - pt2) = ";
	try {
		PointND<int> ptAns2 = pt1 - pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}

	/* Exceeding the limit in the first quadrant */
	outFile << "(pt1 * pt2) = ";
	try {
		PointND<int> ptAns3 = pt1 * pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}


	/** Testing Assertion **/
	/* Processing empty Point */
	PointND<double> emptySet(vector<double> {});
	// PointND<double> assert1 = setDouble3 + emptySet;  // Assertion failed

	/* Processing Points with different dimensions */
	PointND<double> diffSize(vector<double> {1, 2, 3});
	// PointND<double> assert2 = setDouble3 + diffSize;  // Assertion failed

	outFile.close();
	return 0;
}