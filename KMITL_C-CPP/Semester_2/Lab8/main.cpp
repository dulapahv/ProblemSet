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
#include "UnderflowException.h"

int main() {
	ofstream outFile("output.txt");
	assert(outFile);

	/** Testing Point4D Class **/
	Point4D<int> setInt1(1, 2, 3, 4);
	Point4D<int> setInt2(5, 6, 7, 8);
	Point4D<int> setIntLimit(2147483647, 2147483647, 2147483647, 2147483647);
	Point4D<float> setFloat1(10.87, 20.65, 30.43, 40.21);
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
	Point4D<int> sum1 = setInt1 + setInt2;
	Point4D<int> sumS1 = setInt1 + 5;
	outFile << "+ operator method: (setInt1 + setInt2) = "; sum1.print(outFile); outFile << endl;
	outFile << "+ operator method: (setInt1 + 5) = "; sumS1.print(outFile); outFile << endl;

	/* - operator method */
	Point4D<float> diff1 = setFloat1 - setFloat2;
	Point4D<float> diffS1 = setFloat1 - 5.0F;
	outFile << "- operator method: (setFloat1 - setFloat2) = "; diff1.print(outFile); outFile << endl;
	outFile << "- operator method: (setFloat1 - 5.0) = "; diffS1.print(outFile); outFile << endl;

	/* * operator method */
	Point4D<double> prod1 = setDouble1 * setDouble2;
	Point4D<double> prodS1 = setDouble1 * 5.0;
	outFile << "* operator method: (setDouble1 * setDouble2) = "; prod1.print(outFile); outFile << endl;
	outFile << "* operator method: (setDouble1 * 5.0) = "; prodS1.print(outFile); outFile << endl;

	/* / operator method */
	Point4D<double> quot1 = setDouble1 / setDouble2;
	Point4D<double> quotS1 = setDouble1 / 5.0;
	outFile << "/ operator method: (setDouble1 / setDouble2) = "; quot1.print(outFile); outFile << endl;
	outFile << "/ operator method: (setDouble1 / 5.0) = "; quotS1.print(outFile); outFile << endl;

	/* Combining operator methods */
	Point4D<double> mix1 = (((setDouble1 + setDouble2) - 5.0) * setDouble1) / 10.0;
	outFile << "Combining operator methods: ((((setDouble1 + setDouble2) - 5.0) * setDouble1) / 10.0) = "; mix1.print(outFile); outFile << endl;
	
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

	/* Test OverflowException and UnderflowException */
	outFile << "Overflowing a data type: (setInt1 * setIntLimit) = ";
	try {
		Point4D<int> testOver = setInt1 * setIntLimit;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}

	outFile << endl;


	/** Testing PointND Class **/
	PointND<int> setInt3(vector<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
	PointND<int> setInt4(vector<int> { 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 });
	PointND<int> setIntLimit2(vector<int> (10, 2147483647));
	PointND<float> setFloat3(vector<float> { 10.87, 20.65, 30.43, 40.21, 50.01, 60.11, 70.21, 80.31, 90.41, 100.51 });
	PointND<float> setFloat4(vector<float> { 5.21, 6.43, 7.65, 8.87, 9.99, 10.11, 11.23, 12.35, 13.47, 14.59 });
	PointND<double> setDouble3(vector<double> { 1.21, 2.43, 3.65, 4.87, 5.99, 6.11, 7.23, 8.35, 9.47, 10.59 });
	PointND<double> setDouble4(vector<double> { 5.87, 6.65, 7.43, 8.21, 9.01, 10.11, 11.21, 12.31, 13.41, 14.51 });
	PointND<double> setZero2(vector<double> (10, 0));
	PointND<int> pt1(vector<int> { 58, 13 });
	PointND<int> pt2(vector<int> { 9, 60 });

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
	PointND<int> sumS2 = setInt3 + 5;
	outFile << "+ operator method: (setInt3 + setInt4) = "; sum2.print(outFile); outFile << endl;
	outFile << "+ operator method: (setInt3 + 5) = "; sumS2.print(outFile); outFile << endl;

	/* - operator method */
	PointND<float> diff2 = setFloat3 - setFloat4;
	PointND<float> diffS2 = setFloat3 - 5.0F;
	outFile << "- operator method: (setFloat3 - setFloat4) = "; diff2.print(outFile); outFile << endl;
	outFile << "- operator method: (setFloat3 - 5.0) = "; diffS2.print(outFile); outFile << endl;


	/* * operator method */
	PointND<double> prod2 = setDouble3 * setDouble4;
	PointND<double> prodS2 = setDouble3 * 5.0;
	outFile << "* operator method: (setDouble3 * setDouble4) = "; prod2.print(outFile); outFile << endl;
	outFile << "* operator method: (setDouble3 * 5.0) = "; prodS2.print(outFile); outFile << endl;

	/* / operator method */
	PointND<double> quot2 = setDouble3 / setDouble4;
	PointND<double> quotS2 = setDouble3 / 5.0;
	outFile << "/ operator method: (setDouble3 / setDouble4) = "; quot2.print(outFile); outFile << endl;
	outFile << "/ operator method: (setDouble3 / 5.0) = "; quotS2.print(outFile); outFile << endl;

	/* Combining operator methods */
	PointND<double> mix2 = (((setDouble3 + setDouble4) - 5.0) * setDouble3) / 10.0;
	outFile << "Combining operator methods: ((((setDouble3 + setDouble4) - 5.0) * setDouble3) / 10.0) = "; mix2.print(outFile); outFile << endl;

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

	/* Test OverflowException and UnderflowException */
	outFile << "Overflowing a data type: (setInt3 * setIntLimit2) = ";
	try {
		PointND<int> testOver2 = setInt3 * setIntLimit2;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}
	catch (QuadrantException e) {
		noexcept(e);  // This exception is intentionally ignored since we want to test for overflow/underflow exception
	}

	outFile << endl;


	/** Testing QuadrantException Class **/
	// XLIMIT = 500, YLIMIT = 500
	outFile << "Testing Whether The Point Lies In The First Quadrant Or Not (XLIMIT = 500, YLIMIT = 500)" << endl;

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