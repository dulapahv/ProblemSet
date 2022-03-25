#include <fstream>
#include <iostream>
#include <vector>
#include "assert.h"
#include "Point4D.h"
#include "PointND.h"
#include "OverflowException.h"
#include "DivideByZeroException.h"
#include "QuadrantException.h"

using namespace std;

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

	/** Testing Operator Methods **/
	outFile << "Testing Operator Methods" << endl;

	/* + operator method */
	Point4D<int> sum = setInt1 + setInt2;
	outFile << "+ operator method: "; sum.print(outFile); outFile << endl;

	/* - operator method */
	Point4D<float> diff = setFloat1 - setFloat2;
	outFile << "- operator method: "; diff.print(outFile); outFile << endl;

	/* * operator method */
	Point4D<double> prod = setDouble1 * setDouble2;
	outFile << "* operator method: "; prod.print(outFile); outFile << endl;

	/* / operator method */
	Point4D<double> quot = setDouble1 / setDouble2;
	outFile << "/ operator method: "; quot.print(outFile); outFile << endl;

	/* Combining operator methods */
	Point4D<double> mix1 = (((setDouble1 + setDouble2) * setDouble2) - setDouble1) / setDouble2;
	outFile << "Combining operator methods: "; mix1.print(outFile); outFile << endl;
	
	outFile << endl;

	/** Testing Exceptions **/
	outFile << "Testing Exceptions" << endl;

	/* Test DivideByZeroException */
	outFile << "Dividing by zero: ";
	try {
		Point4D<double> testQuot = setDouble1 / setZero;
	}
	catch (DivideByZeroException e) {
		outFile << e.what();
	}

	/* Test OverflowException */
	outFile << "Overflowing a data type: ";
	try {
		Point4D<int> testProd = setInt1 * setIntLimit;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}

	outFile << endl;

	/** Testing PointND Class **/
	PointND<int> setInt3(vector<int>{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
	PointND<int> setInt4(vector<int>{ 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 });
	PointND<int> setIntLimit2(vector<int>{ 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647 });
	PointND<float> setFloat3(vector<float> { 1.87, 2.65, 3.43, 4.21, 5.01, 6.11, 7.21, 8.31, 9.41, 10.51 });
	PointND<float> setFloat4(vector<float> { 5.21, 6.43, 7.65, 8.87, 9.99, 10.11, 11.23, 12.35, 13.47, 14.59 });
	PointND<double> setDouble3(vector<double> { 1.21, 2.43, 3.65, 4.87, 5.99, 6.11, 7.23, 8.35, 9.47, 10.59 });
	PointND<double> setDouble4(vector<double> { 5.87, 6.65, 7.43, 8.21, 9.01, 10.11, 11.21, 12.31, 13.41, 14.51 });
	PointND<double> setZero2(vector<double>(10, 0));

	outFile << "==[Testing PointND Class]===========================================" << endl;

	/** Testing Operator Methods **/
	outFile << "Testing Operator Methods" << endl;

	/* + operator method */
	PointND<int> sum2 = setInt3 + setInt4;
	outFile << "+ operator method: "; sum2.print(outFile); outFile << endl;

	/* - operator method */
	PointND<float> diff2 = setFloat3 - setFloat4;
	outFile << "- operator method: "; diff2.print(outFile); outFile << endl;

	/* * operator method */
	PointND<double> prod2 = setDouble3 * setDouble4;
	outFile << "* operator method: "; prod2.print(outFile); outFile << endl;

	/* / operator method */
	PointND<double> quot2 = setDouble3 / setDouble4;
	outFile << "/ operator method: "; quot2.print(outFile); outFile << endl;

	/* Combining operator methods */
	PointND<double> mix2 = (((setDouble3 + setDouble4) * setDouble4) - setDouble3) / setDouble4;
	outFile << "Combining operator methods: "; mix2.print(outFile); outFile << endl;

	outFile << endl;

	/** Testing Exceptions **/
	outFile << "Testing Exceptions" << endl;

	/* Test DivideByZeroException */
	outFile << "Dividing by zero: ";
	try {
		PointND<double> testQuot2 = setDouble3 / setZero2;
	}
	catch (DivideByZeroException e) {
		outFile << e.what();
	}

	/* Test OverflowException */
	outFile << "Overflowing a data type: ";
	try {
		PointND<int> testProd2 = setInt3 * setIntLimit2;
	}
	catch (OverflowException e) {
		outFile << e.what();
	}

	outFile << endl;


	/** Testing Assertion **/
	/* Processing empty Point */
	PointND<double> emptySet(vector<double> {});
	// PointND<double> assert1 = setDouble3 + emptySet;  // Assertion failed

	/* Processing Points with different dimensions */
	PointND<double> diffSize(vector<double> {1, 2, 3});
	// PointND<double> assert2 = setDouble3 + diffSize;  // Assertion failed


	/** Testing QuadrantException Class **/
	// XLIMIT = 50, YLIMIT = 50
	outFile << "Testing Whether The Point Lies In The First Quadrant Or Not" << endl;

	PointND<int> pt1(vector<int> { 12, 2 });
	PointND<int> pt2(vector<int> { 5, 8 });

	/* In the first quadrant */
	try {
		PointND<int> ptAns1 = pt1 + pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}

	/* Not in the first quadrant */
	try {
		PointND<int> ptAns2 = pt1 - pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}

	/* Exceeding the limit in the first quadrant */
	try {
		PointND<int> ptAns3 = pt1 * pt2;
		outFile << "Point is in the first quadrant" << endl;
	}
	catch (QuadrantException e) {
		outFile << e.what();
	}

	outFile.close();
	return 0;
}