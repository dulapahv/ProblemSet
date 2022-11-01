// // #include <iostream>
// // int main()
// // {
// //   float a = 5.51;
// //   int b = static_cast<int>(a);
// //   std::cout << b;
// // }

// // #include <iostream>

// // using namespace std;

// // class A {
// // public:
// // 	virtual void show() {
// // 		cout << "Base class";
// // 	}
// // };

// // class B : public A {
// // public:
// // 	void show() {
// // 		cout << "Derived Class";
// // 	}
// // };

// // int main() {
// // 	A *ptr;		 // Early binding because pointer is of type A
// // 	ptr = new B; // Late binding because object is not known at compile time.
// // 	ptr->show(); // Early binding
// // }

// // #include <iostream>

// // using namespace std;

// // class Test {
// // public:
// // 	virtual void show() {
// // 		cout << "Base class" << endl;
// // 	}
// // };

// // class Derived : public Test {
// // public:
// // 	void show() {
// // 		cout << "Derived Class" << endl;
// // 	}
// // };

// // int main() {
// // 	Test *t;   // Base class pointer
// // 	Derived d; // Derived class object
// // 	t = &d;	   // Pointing base class pointer to derived class
// // 	t->show(); // Late binding

// // 	return 0;
// // }

// // #include <iostream>
// // #include <iomanip>

// // using namespace std;

// // bool compare_two_methods(double x, double y)
// // {
// // 	double a = x; /** Compute a with method A **/
// // 	double b = y; /* Compute b with method B **/
// // 	/** Was the answer the same? **/
// // 	bool match = (a == b);
// // 	return match;
// // }

// // int main()
// // {
// // 	cout << "The answer is " << compare_two_methods(2.0, 5.0) << endl;
// // }

// // bool compare_two_methods(double x, double y) {
// //   double a = x; /** Compute a with method A **/
// //   double b = y; /* Compute b with method B **/
// //    /** Was the answer the same? **/
// //    bool match = std::abs(a - b) < std::numeric_limits<double>::epsilon();
// //    return match;
// // }

// // assert((month >= 1)&&(month <= 12));
// // assert((days worked >= 0)&&(days worked <=31));
// // assert(lut != NULL);

// // const double EPS = 0.00001;

// // boolean compare_two_methods(...) {
// //   double a = fa(...); /** Compute a with method A **/
// //   double b = fb(...); /* Compute b with method B **/
// //    /** Was the answer the same? **/
// //    boolean match = (abs(a-b) < EPS);
// //    return match;
// //    }

// // class Vehicle { /** Common properties of vehicles **/
// // 	..
// // };
// // class Engine { /** Models various types of engines **/
// // 	....
// // };
// // class Car {
// // private:
// // 	Engine engine;

// // public:
// // 	Car() : engine(){};
// // };
// // class Train {
// // private:
// // 	Engine engine;

// // public:
// // 	Train() : engine(){};
// // };

// // #include “SalaryLUT.h”
// // class Employee: public Person {
// // private:
// //     int level; // Salary level
// //     SalaryLUT *lut;
// // 	..../** lots of code omitted **/
// // public:
// //     double getSalary(int month, int days_worked) {
// // 	assert((month >= 1) && (month <= 12));
// // 	assert((days worked >= 0) && (days worked <= 31));
// // 	assert(lut != NULL);
// // 	double s = lut->calcSalary(level, month, days_wored);
// // 	assert(s > 0);
// // 	return s;
// //     }
// // };

// #include <stdio.h>
// #define _USE_MATH_DEFINES
// #include <math.h>
// #include <windows.h>

// // width and height of screen
// #define ww 100
// #define wh 50

// void clr(CHAR_INFO* d)
// {
// 	for (int i = 0; i < ww * wh; ++i)
// 	{
// 		d[i].Attributes = FOREGROUND_GREEN;
// 		d[i].Char.UnicodeChar = ' ';
// 	}
// }

// void set(CHAR_INFO* d, COORD pt, char c)
// {
// 	d[pt.Y * ww + pt.X].Char.UnicodeChar = c;
// }

// char getp(CHAR_INFO* d, COORD* pts, double err)
// {
// 	if (abs(pts[0].Y - pts[2].Y) < 2)
// 	{
// 		if (err > 0.5)
// 		{
// 			return '-';
// 		}
// 		return '_';
// 	}

// 	if (abs(pts[0].X - pts[2].X) < 2 &&
// 		(pts[0].X >= pts[2].X || pts[1].X != pts[2].X) &&
// 		(pts[0].X <= pts[2].X || pts[1].X != pts[0].X))
// 	{
// 		return '|';
// 	}

// 	int mX = pts[0].Y < pts[2].Y ? pts[0].X : pts[2].X;
// 	return mX < pts[1].X ? '\\' : '/';\
// }

// void ln(CHAR_INFO* d, COORD a, COORD b)
// {
// 	set(d, a, '@');
// 	set(d, b, '@');

// 	int dx = abs(b.X - a.X), sx = a.X < b.X ? 1 : -1;
// 	int dy = abs(b.Y - a.Y), sy = a.Y < b.Y ? 1 : -1;
// 	int err = (dx > dy ? dx : -dy) / 2, e2;

// 	COORD pts[3];
// 	double ers[3];

// 	for (int i = 0; i < 3; ++i)
// 	{
// 		pts[i] = a;
// 		ers[i] = ((double)err - dx) / ((double)dy - dx);
// 		ers[i] = sy == 1 ? 1.0f - ers[i] : ers[i];

// 		if (a.X == b.X && a.Y == b.Y) {
// 			return;
// 		}

// 		e2 = err;
// 		if (e2 > -dx) { err -= dy; a.X += sx; }
// 		if (e2 < dy) { err += dx; a.Y += sy; }
// 	}

// 	for (;;)
// 	{
// 		set(d, pts[1], getp(d, pts, ers[1]));

// 		pts[0] = pts[1];
// 		pts[1] = pts[2];
// 		pts[2] = a;

// 		ers[0] = ers[1];
// 		ers[1] = ers[2];
// 		ers[2] = ((double)err - dx) / ((double)dy - dx);
// 		ers[2] = sy == 1 ? 1.0f - ers[2] : ers[2];

// 		if (a.X == b.X && a.Y == b.Y) {
// 			break;
// 		}

// 		e2 = err;
// 		if (e2 > -dx) { err -= dy; a.X += sx; }
// 		if (e2 < dy) { err += dx; a.Y += sy; }
// 	}

// 	// add the final point
// 	set(d, pts[1], getp(d, pts, ers[1]));
// }

// // hypercube vertices in 4D
// double V4[16][4] =
// {
// 	{-1, -1, -1, -1},
// 	{ 1, -1, -1, -1},
// 	{-1,  1, -1, -1},
// 	{ 1,  1, -1, -1},
// 	{-1, -1,  1, -1},
// 	{ 1, -1,  1, -1},
// 	{-1,  1,  1, -1},
// 	{ 1,  1,  1, -1},
// 	{-1, -1, -1,  1},
// 	{ 1, -1, -1,  1},
// 	{-1,  1, -1,  1},
// 	{ 1,  1, -1,  1},
// 	{-1, -1,  1,  1},
// 	{ 1, -1,  1,  1},
// 	{-1,  1,  1,  1},
// 	{ 1,  1,  1,  1},
// };

// // store the vertices once they have been projected to 3D
// double V3[16][3];

// // final 2D projection
// double V2[16][2];

// // the indices for each line
// int indices[32][2] =
// {
// 	// cube #1
// 	{0, 1},
// 	{0, 2},
// 	{0, 4},
// 	{1, 3},
// 	{1, 5},
// 	{2, 3},
// 	{2, 6},
// 	{3, 7},
// 	{4, 5},
// 	{4, 6},
// 	{5, 7},
// 	{6, 7},

// 	// in-between lines
// 	{0,	8},
// 	{1,	9},
// 	{2,	10},
// 	{3,	11},
// 	{4,	12},
// 	{5,	13},
// 	{6,	14},
// 	{7,	15},

// 	// cube #2
// 	{8, 9},
// 	{8, 10},
// 	{8, 12},
// 	{9, 11},
// 	{9, 13},
// 	{10, 11},
// 	{10, 14},
// 	{11, 15},
// 	{12, 13},
// 	{12, 14},
// 	{13, 15},
// 	{14, 15},
// };

// double dot4(const double* V, const double* U)
// {
// 	return (V[0] * U[0]) + (V[1] * U[1]) + (V[2] * U[2]) + (V[3] * U[3]);
// }

// double norm4(const double* V)
// {
// 	return sqrt(dot4(V, V));
// }

// // cross4 computes the four-dimensional cross product of the three vectors
// // U, V and W, in that order.
// // returns the resulting four-vector.
// void cross4(double* result, const double* U, const double* V, const double* W)
// {
// 	// intermediate values
// 	double A, B, C, D, E, F;

// 	// calculate intermediate values
// 	A = (V[0] * W[1]) - (V[1] * W[0]);
// 	B = (V[0] * W[2]) - (V[2] * W[0]);
// 	C = (V[0] * W[3]) - (V[3] * W[0]);
// 	D = (V[1] * W[2]) - (V[2] * W[1]);
// 	E = (V[1] * W[3]) - (V[3] * W[1]);
// 	F = (V[2] * W[3]) - (V[3] * W[2]);

// 	// calculate the result-vector components
// 	result[0] = (U[1] * F) - (U[2] * E) + (U[3] * D);
// 	result[1] = -(U[0] * F) + (U[2] * C) - (U[3] * B);
// 	result[2] = (U[0] * E) - (U[1] * C) + (U[3] * A);
// 	result[3] = -(U[0] * D) + (U[1] * B) - (U[2] * A);
// }

// void vecSub4(double* result, const double* a, const double* b)
// {
// 	result[0] = a[0] - b[0];
// 	result[1] = a[1] - b[1];
// 	result[2] = a[2] - b[2];
// 	result[3] = a[3] - b[3];
// }

// void vecScale4(double* vec, double m)
// {
// 	vec[0] *= m;
// 	vec[1] *= m;
// 	vec[2] *= m;
// 	vec[3] *= m;
// }

// void matVecMul4(double* result, const double* mat, const double* vec)
// {
// 	for (int row = 0; row < 4; ++row)
// 	{
// 		result[row] = 0;
// 		for (int col = 0; col < 4; ++col)
// 		{
// 			result[row] += mat[col * 4 + row] * vec[col];
// 		}
// 	}
// }

// // creates a rotation matrix for the XW plane
// // T is the angle in radians
// void rotXW4(double* result, double T)
// {
// 	// column vectors
// 	double* Wa = result + 4 * 0;
// 	double* Wb = result + 4 * 1;
// 	double* Wc = result + 4 * 2;
// 	double* Wd = result + 4 * 3;

// 	Wa[0] = cos(T);
// 	Wa[1] = 0;
// 	Wa[2] = 0;
// 	Wa[3] = -sin(T);

// 	Wb[0] = 0;
// 	Wb[1] = 1;
// 	Wb[2] = 0;
// 	Wb[3] = 0;

// 	Wc[0] = 0;
// 	Wc[1] = 0;
// 	Wc[2] = 1;
// 	Wc[3] = 0;

// 	Wd[0] = sin(T);
// 	Wd[1] = 0;
// 	Wd[2] = 0;
// 	Wd[3] = cos(T);
// }

// double from4[4] = { 5, 0, 0, 0 };
// double to4[4] = { 0, 0, 0, 0 };
// double up4[4] = { 0, 1, 0, 0 };
// double over4[4] = { 0, 0, 1, 0 };

// // generate a 4D view matrix
// void view4(double* result)
// {
// 	// column vectors
// 	double* Wa = result + 4 * 0;
// 	double* Wb = result + 4 * 1;
// 	double* Wc = result + 4 * 2;
// 	double* Wd = result + 4 * 3;

// 	// vector norm
// 	double norm;

// 	// get the normalized Wd column-vector.
// 	vecSub4(Wd, to4, from4);
// 	norm = norm4(Wd);
// 	vecScale4(Wd, 1 / norm);

// 	// calculate the normalized Wa column-vector.
// 	cross4(Wa, up4, over4, Wd);
// 	norm = norm4(Wa);
// 	vecScale4(Wa, 1 / norm);

// 	// calculate the normalized Wb column-vector.
// 	cross4(Wb, over4, Wd, Wa);
// 	norm = norm4(Wb);
// 	vecScale4(Wb, 1 / norm);

// 	// calculate the Wc column-vector.
// 	cross4(Wc, Wd, Wa, Wb);
// }

// void projectTo3D(double vAngle, const double* matView, const double* matRotation)
// {
// 	// column vectors
// 	const double* Wa = matView + 4 * 0;
// 	const double* Wb = matView + 4 * 1;
// 	const double* Wc = matView + 4 * 2;
// 	const double* Wd = matView + 4 * 3;

// 	// divisor Values
// 	double S, T;

// 	T = 1 / tan(vAngle / 2);

// 	for (int i = 0; i < 16; ++i)
// 	{
// 		double V[4];
// 		matVecMul4(V, matRotation, V4[i]);

// 		double Vf[4];
// 		vecSub4(Vf, V, from4);

// 		S = T / dot4(Vf, Wd);

// 		V3[i][0] = S * dot4(Vf, Wa);
// 		V3[i][1] = S * dot4(Vf, Wb);
// 		V3[i][2] = S * dot4(Vf, Wc);
// 	}
// }

// double dot3(const double* V, const double* U)
// {
// 	return (V[0] * U[0]) + (V[1] * U[1]) + (V[2] * U[2]);
// }

// double norm3(const double* V)
// {
// 	return sqrt(dot3(V, V));
// }

// void cross3(double* result, const double* U, const double* V)
// {
// 	result[0] = (U[1] * V[2]) - (U[2] * V[1]);
// 	result[1] = (U[2] * V[0]) - (U[0] * V[2]);
// 	result[2] = (U[0] * V[1]) - (U[1] * V[0]);
// }
// void vecSub3(double* result, const double* a, const double* b)
// {
// 	result[0] = a[0] - b[0];
// 	result[1] = a[1] - b[1];
// 	result[2] = a[2] - b[2];
// }

// void vecScale3(double* vec, double m)
// {
// 	vec[0] *= m;
// 	vec[1] *= m;
// 	vec[2] *= m;
// }

// void matVecMul3(double* result, const double* mat, const double* vec)
// {
// 	for (int row = 0; row < 3; ++row)
// 	{
// 		result[row] = 0;
// 		for (int col = 0; col < 3; ++col)
// 		{
// 			result[row] += mat[col * 3 + row] * vec[col];
// 		}
// 	}
// }

// void rotXZ3(double* result, double T)
// {
// 	// column vectors
// 	double* Va = result + 3 * 0;
// 	double* Vb = result + 3 * 1;
// 	double* Vc = result + 3 * 2;

// 	Va[0] = cos(T);
// 	Va[1] = 0;
// 	Va[2] = -sin(T);

// 	Vb[0] = 0;
// 	Vb[1] = 1;
// 	Vb[2] = 0;

// 	Vc[0] = sin(T);
// 	Vc[1] = 0;
// 	Vc[2] = cos(T);
// }

// double from3[3] = { 3.00f, 0.99f, 1.82f };
// double to3[3] = { 0, 0, 0 };
// double up3[3] = { 0, -1, 0 };

// // generate a 3D view matrix
// void view3(double* result)
// {
// 	double* Va = result + 3 * 0;
// 	double* Vb = result + 3 * 1;
// 	double* Vc = result + 3 * 2;

// 	double norm;

// 	// Get the normalized Vc column-vector.
// 	vecSub3(Vc, to3, from3);
// 	norm = norm3(Vc);
// 	vecScale3(Vc, 1 / norm);

// 	// Calculate the normalized Va column-vector.
// 	cross3(Va, Vc, up3);
// 	norm = norm3(Va);
// 	vecScale3(Va, 1 / norm);

// 	// Calculate the Vb column-vector.
// 	cross3(Vb, Va, Vc);
// }

// void projectTo2D(double vAngle, const double* matView, const double* matRotation)
// {
// 	// column vectors
// 	const double* Va = matView + 3 * 0;
// 	const double* Vb = matView + 3 * 1;
// 	const double* Vc = matView + 3 * 2;

// 	// divisor values
// 	double  S, T;

// 	T = 1 / tan(vAngle / 2);

// 	for (int i = 0; i < 16; ++i)
// 	{
// 		double V[3];
// 		matVecMul3(V, matRotation, V3[i]);

// 		double Vf[3];
// 		vecSub3(Vf, V, from3);

// 		S = T / dot3(Vf, Vc);

// 		V2[i][0] = (ww / 2) + (ww * S * dot3(Vf, Va));
// 		V2[i][1] = (wh / 2) + (wh * S * dot3(Vf, Vb));
// 	}
// }

// int main(int argc, const char* argv[])
// {
// 	// get the console handle
// 	HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);

// 	// set console dimensions
// 	COORD s = { ww, wh };
// 	SMALL_RECT r = { 0, 0, ww, wh };
// 	COORD z = { 0, 0 };
// 	SetConsoleScreenBufferSize(h, s);
// 	SetConsoleWindowInfo(h, TRUE, &r);

// 	CHAR_INFO d[wh * ww];

// 	double viewMat4[4 * 4];
// 	view4(viewMat4);
// 	double rot4[4 * 4];

// 	double viewMat3[3 * 3];
// 	view3(viewMat3);
// 	double rot3[3 * 3];

// 	double rotation = 0;

// 	for (;;)
// 	{
// 		rotation += 0.01f;

// 		rotXW4(rot4, rotation);
// 		projectTo3D(M_PI / 3, viewMat4, rot4);

// 		rotXZ3(rot3, rotation * 0.3);
// 		projectTo2D(M_PI / 4, viewMat3, rot3);

// 		clr(d);

// 		for (int i = 0; i < 32; ++i)
// 		{
// 			int a = indices[i][0];
// 			int b = indices[i][1];
// 			COORD c1 = { (SHORT)V2[a][0], (SHORT)V2[a][1] };
// 			COORD c2 = { (SHORT)V2[b][0], (SHORT)V2[b][1] };
// 			ln(d, c1, c2);
// 		}

// 		WriteConsoleOutput(h, d, s, z, &r);

// 		Sleep(1);
// 	}
// }

// #include <stdio.h>
// #include <stdlib.h>

// #define UNASSIGNED 0
// #define N 4

// //finds an unassigned location in grid
// bool FindUnassignedLocation(int grid[N][N], int *row, int *col);

// // Checks whether it will be legal to assign num to the given row, col
// bool isSafe(int grid[N][N], int row, int col, int num);

// /* Takes a partially filled-in grid and attempts to assign values to
//   all unassigned locations in such a way to meet the requirements
//   for Sudoku solution (non-duplication across rows, columns, and boxes) */
// bool SolveSudoku(int grid[N][N])
// {
//     int row, col;

//     // If there is no unassigned location, we are done
//     if (!FindUnassignedLocation(grid, &row, &col))
//        return true; // success!

//     // consider digits 1 to 9
//     for (int num = 1; num <= 9; num++)
//     {
//         // if looks promising
//         if (isSafe(grid, row, col, num))
//         {
//             // make tentative assignment
//             grid[row][col] = num;

//             // return, if success, yay!
//             if (SolveSudoku(grid))
//                 return true;

//             // failure, unmake & try again
//             grid[row][col] = UNASSIGNED;
//         }
//     }
//     return false; // this triggers backtracking
// }

// /* Searches the grid to find an entry that is still unassigned. If
//    found, the reference parameters row, col will be set the location
//    that is unassigned, and true is returned. If no unassigned entries
//    remain, false is returned. */
// bool FindUnassignedLocation(int grid[N][N], int *row, int *col)
// {
//     for (*row = 0; *row < N; (*row)++)
//         for (*col = 0; *col < N; (*col)++)
//             if (grid[*row][*col] == UNASSIGNED)
//                 return true;
//     return false;
// }

// /* Returns a boolean which indicates whether any assigned entry
//    in the specified row matches the given number. */
// bool UsedInRow(int grid[N][N], int row, int num)
// {
//     for (int col = 0; col < N; col++)
//         if (grid[row][col] == num)
//             return true;
//     return false;
// }

// /* Returns a boolean which indicates whether any assigned entry
//    in the specified column matches the given number. */
// bool UsedInCol(int grid[N][N], int col, int num)
// {
//     for (int row = 0; row < N; row++)
//         if (grid[row][col] == num)
//             return true;
//     return false;
// }

// /* Returns a boolean which indicates whether any assigned entry
//    within the specified 3x3 box matches the given number. */
// bool UsedInBox(int grid[N][N], int boxStartRow, int boxStartCol, int num)
// {
//     for (int row = 0; row < 3; row++)
//         for (int col = 0; col < 3; col++)
//             if (grid[row+boxStartRow][col+boxStartCol] == num)
//                 return true;
//     return false;
// }

// /* Returns a boolean which indicates whether it will be legal to assign
//    num to the given row, col location. */
// bool isSafe(int grid[N][N], int row, int col, int num)
// {
//     /* Check if 'num' is not already placed in current row,
//        current column and current 3x3 box */
//     return !UsedInRow(grid, row, num) &&
//            !UsedInCol(grid, col, num) &&
//            !UsedInBox(grid, row - row%3 , col - col%3, num);
// }

// /* A utility function to print grid  */
// void printGrid(int grid[N][N])
// {
//     for (int row = 0; row < N; row++)
//     {
//        for (int col = 0; col < N; col++)
//              printf("%2d", grid[row][col]);
//         printf("\n");
//     }
// }

// /* Driver Program to test above functions */
// int main()
// {
//     // 0 means unassigned cells
//     int grid[N][N] = {{1, 2, 3, 4},
// 					  {2, 3, 4, 0},
// 					  {3, 4, 1, 0},
// 					  {4, 1, 2, 0}};
//     if (SolveSudoku(grid) == true)
//           printGrid(grid);
//     else
//          printf("No solution exists");

//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// #define true 1
// #define false 0
// #define N 4

// // function to check if a given row is valid
// int check_row(int grid[N][N], int row, int num)
// {
//     int j;

//     for (j = 0; j < N; j++)
//     {
//         if (grid[row][j] == num)
//         {
//             return false;
//         }
//     }

//     return true;
// }

// // function to check if a given column is valid
// int check_col(int grid[N][N], int col, int num)
// {
//     int i;

//     for (i = 0; i < N; i++)
//     {
//         if (grid[i][col] == num)
//         {
//             return false;
//         }
//     }

//     return true;
// }

// // function to check if a given row satisfies the given constraints
// int check_row_constraints(int grid[N][N], int row_constraints[N][N], int row)
// {
//     int i, j, num, count;

//     for (i = 0; i < N; i++)
//     {
//         num = row_constraints[row][i];
//         count = 0;

//         if (num == 0)
//         {
//             continue;
//         }

//         for (j = 0; j < N; j++)
//         {
//             if (grid[row][j] > num)
//             {
//                 count++;
//             }
//         }

//         if (count != num)
//         {
//             return false;
//         }
//     }

//     return true;
// }

// // function to check if a given column satisfies the given constraints
// int check_col_constraints(int grid[N][N], int col_constraints[N][N], int col)
// {
//     int i, j, num, count;

//     for (i = 0; i < N; i++)
//     {
//         num = col_constraints[col][i];
//         count = 0;

//         if (num == 0)
//         {
//             continue;
//         }

//         for (j = 0; j < N; j++)
//         {
//             if (grid[j][col] > num)
//             {
//                 count++;
//             }
//         }

//         if (count != num)
//         {
//             return false;
//         }
//     }

//     return true;
// }

// // function to solve the skyscrapers puzzle
// int solve_skyscrapers(int grid[N][N], int row_constraints[N][N], int col_constraints[N][N], int row, int col)
// {
//     int num;

//     // if we have reached the last cell, return true
//     if (row == N - 1 && col == N - 1)
//     {
//         return true;
//     }

//     // if we have reached the end of a row, move to the next row
//     if (col == N)
//     {
//         row++;
//         col = 0;
//     }

//     // if the current cell is not empty, try solving the next cell
//     if (grid[row][col] != 0)
//     {
//         return solve_skyscrapers(grid, row_constraints, col_constraints, row, col + 1);
//     }

//     // consider all possible values for the current cell
//     for (num = 1; num <= N; num++)
//     {
//         // check if the given value is valid for the current cell
//         if (check_row(grid, row, num) && check_col(grid, col, num) && check_row_constraints(grid, row_constraints, row) && check_col_constraints(grid, col_constraints, col))
//         {
//             // if the value is valid, assign it to the current cell
//             grid[row][col] = num;

//             // try solving the next cell
//             if (solve_skyscrapers(grid, row_constraints, col_constraints, row, col + 1))
//             {
//                 return true;
//             }
//             else
//             {
//                 // if the next cell cannot be solved, backtrack
//                 grid[row][col] = 0;
//             }
//         }
//     }

//     // if no value is valid for the current cell, return false
//     return false;
// }

// int main()
// {
//     int grid[N][N];

//     // row constraints
//     int row_constraints[N][N] = {{3, 2, 1, 3},
//                                  {2, 3, 2, 2},
//                                  {2, 1, 2, 3},
//                                  {3, 2, 1, 3}};

//     // column constraints
//     int col_constraints[N][N] = {{1, 2, 2, 3},
//                                  {2, 1, 2, 3},
//                                  {3, 2, 3, 2},
//                                  {2, 2, 1, 2}};

//     int i, j;

//     // initialize grid
//     for (i = 0; i < N; i++)
//     {
//         for (j = 0; j < N; j++)
//         {
//             grid[i][j] = 0;
//         }
//     }

//     // backtracking
//     if (solve_skyscrapers(grid, row_constraints, col_constraints, 0, 0))
//     {
//         // print solution
//         for (i = 0; i < N; i++)
//         {
//             for (j = 0; j < N; j++)
//             {
//                 printf("%d ", grid[i][j]);
//             }
//             printf("\n");
//         }
//     }
//     else
//     {
//         printf("No solution exists\n");
//     }

//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main(int argc, char *argv[])

// {

// 	int i, j, k;

// 	int a[16] = {0}; // array to store the numbers

// 	int b[4][4] = {{0}}; // array to store the constraints

// 	// input the numbers

// 	// for (i = 0; i < 16; i++)

// 	// {

// 	// 	scanf("%d", &a[i]);
// 	// }

// 	// input the constraints

// 	for (i = 0; i < 4; i++)

// 	{

// 		for (j = 0; j < 4; j++)

// 		{

// 			scanf("%d", &b[i][j]);
// 		}
// 	}

// 	// check if the input is valid

// 	for (i = 0; i < 16; i++)

// 	{

// 		if (a[i] < 1 || a[i] > 4)

// 		{

// 			printf("Invalid input\n");

// 			return 0;
// 		}
// 	}

// 	// check if the constraints are valid

// 	for (i = 0; i < 4; i++)

// 	{

// 		for (j = 0; j < 4; j++)

// 		{

// 			if (b[i][j] < 0 || b[i][j] > 4)

// 			{

// 				printf("Invalid input\n");

// 				return 0;
// 			}
// 		}
// 	}

// 	// solve the puzzle

// 	for (i = 0; i < 4; i++)

// 	{

// 		// check the constraint on the left side

// 		if (b[i][0] != 0)

// 		{

// 			int max = 0;

// 			for (j = 0; j < b[i][0]; j++)

// 			{

// 				if (a[i * 4 + j] > max)

// 				{

// 					max = a[i * 4 + j];
// 				}
// 			}

// 			if (max != b[i][0])

// 			{

// 				printf("No solution\n");

// 				return 0;
// 			}
// 		}

// 		// check the constraint on the right side

// 		if (b[i][1] != 0)

// 		{

// 			int max = 0;

// 			for (j = 0; j < b[i][1]; j++)

// 			{

// 				if (a[i * 4 + 3 - j] > max)

// 				{

// 					max = a[i * 4 + 3 - j];
// 				}
// 			}

// 			if (max != b[i][1])

// 			{

// 				printf("No solution\n");

// 				return 0;
// 			}
// 		}

// 		// check the constraint on the top side

// 		if (b[0][i] != 0)

// 		{

// 			int max = 0;

// 			for (j = 0; j < b[0][i]; j++)

// 			{

// 				if (a[i + j * 4] > max)

// 				{

// 					max = a[i + j * 4];
// 				}
// 			}

// 			if (max != b[0][i])

// 			{

// 				printf("No solution\n");

// 				return 0;
// 			}
// 		}

// 		// check the constraint on the bottom side

// 		if (b[1][i] != 0)

// 		{

// 			int max = 0;

// 			for (j = 0; j < b[1][i]; j++)

// 			{

// 				if (a[3 - i + j * 4] > max)

// 				{

// 					max = a[3 - i + j * 4];
// 				}
// 			}

// 			if (max != b[1][i])

// 			{

// 				printf("No solution\n");

// 				return 0;
// 			}
// 		}
// 	}

// 	// print the solution

// 	for (i = 0; i < 4; i++)

// 	{

// 		for (j = 0; j < 4; j++)
// 		{

// 			printf("%d ", a[i * 4 + j]);
// 		}

// 		printf("\n");
// 	}

// 	return 0;
// }

/*
Rules:

The numbers 1-4 must appear once and only once in each row and column.
The numbers 1-4 must appear in each of the four corners.
No two rows or columns may contain the same numbers.
*/

// #include <stdio.h>

// int main() {

// int grid[4][4];
// int side_constraints[4][4];

// int print, i, j, k, l;
// int valid = 1;

// printf("Enter side constraints (top, right, bottom, left):\n");

// for (i=0; i<4; i++) {
//   for (j=0; j<4; j++) {
//     scanf("%d", &side_constraints[i][j]);
//   }
// }

// // Check if constraints are valid
// for (i=0; i<4; i++) {
//   for (j=0; j<4; j++) {
//     if (side_constraints[i][j] < 0 || side_constraints[i][j] > 4) {
//       valid = 0;
//       break;
//     }
//   }
// }

// if (valid) {
//   // Initialize grid
//   for (i=0; i<4; i++) {
//     for (j=0; j<4; j++) {
//       grid[i][j] = 0;
//     }
//   }

//   // Top
//   for (i=0; i<4; i++) {
//     for (j=0; j<4; j++) {
//       if (side_constraints[0][i] == j+1) {
//         grid[0][i] = j+1;
//       }
//     }
//   }

//   // Right
//   for (i=0; i<4; i++) {
//     for (j=0; j<4; j++) {
//       if (side_constraints[1][i] == j+1) {
//         grid[i][3] = j+1;
//       }
//     }
//   }

//   // Bottom
//   for (i=0; i<4; i++) {
//     for (j=0; j<4; j++) {
//       if (side_constraints[2][i] == j+1) {
//         grid[3][i] = j+1;
//       }
//     }
//   }

//   // Left
//   for (i=0; i<4; i++) {
//     for (j=0; j<4; j++) {
//       if (side_constraints[3][i] == j+1) {
//         grid[i][0] = j+1;
//       }
//     }
//   }

//   // Check if corners are valid
//   if (grid[0][0] != 0 && grid[0][3] != 0 && grid[3][0] != 0 && grid[3][3] != 0) {
//     valid = 1;
//   }
//   else {
//     valid = 0;
//   }

//   // Check if rows and columns are valid
//   if (valid) {
//     for (i=0; i<4; i++) {
//       for (j=0; j<4; j++) {
//         for (k=0; k<4; k++) {
//           if (k != i && grid[i][j] == grid[k][j]) {
//             valid = 0;
//             break;
//           }
//         }
//         if (!valid) {
//           break;
//         }
//         for (k=0; k<4; k++) {
//           if (k != j && grid[i][j] == grid[i][k]) {
//             valid = 0;
//             break;
//           }
//         }
//         if (!valid) {
//           break;
//         }
//       }
//       if (!valid) {
//         break;
//       }
//     }
//   }

//   if (valid) {
//     printf("Grid:\n");
//     for (i=0; i<4; i++) {
//       for (j=0; j<4; j++) {
//         printf("%d ", grid[i][j]);
//       }
//       printf("\n");
//     }
//   }
//   else {
//     printf("Invalid constraints\n");
//   }
// }
// else {
//   printf("Invalid constraints\n");
// }

// return 0;

// }

// #include <stdio.h>
// #include <string.h>

// int main(int argc, char **argv)
// {
//     if (argc != 2)
//     {
//         printf("\n");
//         return (0);
//     }
//     int i = 0;
//     int last = 0;
//     while (argv[1][i])
//     {
//         if ((argv[1][i] == ' ' || argv[1][i] == '\t') && (argv[1][i + 1] != ' ' && argv[1][i + 1] != '\t' && argv[1][i + 1] != '\0'))
//             last = i + 1;
//         i++;
//     }
//     while (argv[1][last] && argv[1][last] != ' ' && argv[1][last] != '\t')
//         last++;
//     argv[1][last] = '\0';
//     printf("%s\n", &(argv[1][last]));
//     return (0);
// }


// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     int grid[4][4]; //the 4x4 grid that will be used to store the numbers
    
//     //the constraints for each side of the grid
//     int top[4] = {4, 3, 2, 1};
//     int bottom[4] = {1, 2, 3, 4};
//     int left[4] = {2, 1, 4, 3};
//     int right[4] = {3, 4, 1, 2};
    
//     //initializing the grid to all zeroes
//     int i, j;
//     for(i=0; i<4; i++)
//     {
//         for(j=0; j<4; j++)
//         {
//             grid[i][j] = 0;
//         }
//     }
    
//     //solving the puzzle by checking the constraints for each side
//     //and placing the numbers in the grid
    
//     //checking the top side constraints
//     for(i=0; i<4; i++)
//     {
//         //the first and last row will only have one number that satisfies the constraint
//         if(i==0 || i==3)
//         {
//             for(j=0; j<4; j++)
//             {
//                 if(top[i] == (j+1))
//                 {
//                     grid[i][j] = top[i];
//                 }
//             }
//         }
        
//         //for the second and third row, there will be two numbers that satisfy the constraint
//         else
//         {
//             int count = 0;
//             for(j=0; j<4; j++)
//             {
//                 if(top[i] == (j+1))
//                 {
//                     grid[i][j] = top[i];
//                     count++;
//                 }
//             }
            
//             //if there is only one number that satisfies the constraint, the other one will be on the opposite side
//             if(count == 1)
//             {
//                 for(j=0; j<4; j++)
//                 {
//                     if(grid[i][j] == 0)
//                     {
//                         grid[i][j] = top[i];
//                     }
//                 }
//             }
//         }
//     }
    
//     //checking the bottom side constraints
//     for(i=0; i<4; i++)
//     {
//         //the first and last row will only have one number that satisfies the constraint
//         if(i==0 || i==3)
//         {
//             for(j=0; j<4; j++)
//             {
//                 if(bottom[i] == (j+1))
//                 {
//                     grid[i][j] = bottom[i];
//                 }
//             }
//         }
        
//         //for the second and third row, there will be two numbers that satisfy the constraint
//         else
//         {
//             int count = 0;
//             for(j=0; j<4; j++)
//             {
//                 if(bottom[i] == (j+1))
//                 {
//                     grid[i][j] = bottom[i];
//                     count++;
//                 }
//             }
            
//             //if there is only one number that satisfies the constraint, the other one will be on the opposite side
//             if(count == 1)
//             {
//                 for(j=0; j<4; j++)
//                 {
//                     if(grid[i][j] == 0)
//                     {
//                         grid[i][j] = bottom[i];
//                     }
//                 }
//             }
//         }
//     }
    
//     //checking the left side constraints
//     for(i=0; i<4; i++)
//     {
//         //the first and last column will only have one number that satisfies the constraint
//         if(i==0 || i==3)
//         {
//             for(j=0; j<4; j++)
//             {
//                 if(left[i] == (j+1))
//                 {
//                     grid[j][i] = left[i];
//                 }
//             }
//         }
        
//         //for the second and third column, there will be two numbers that satisfy the constraint
//         else
//         {
//             int count = 0;
//             for(j=0; j<4; j++)
//             {
//                 if(left[i] == (j+1))
//                 {
//                     grid[j][i] = left[i];
//                     count++;
//                 }
//             }
            
//             //if there is only one number that satisfies the constraint, the other one will be on the opposite side
//             if(count == 1)
//             {
//                 for(j=0; j<4; j++)
//                 {
//                     if(grid[j][i] == 0)
//                     {
//                         grid[j][i] = left[i];
//                     }
//                 }
//             }
//         }
//     }
    
//     //checking the right side constraints
//     for(i=0; i<4; i++)
//     {
//         //the first and last column will only have one number that satisfies the constraint
//         if(i==0 || i==3)
//         {
//             for(j=0; j<4; j++)
//             {
//                 if(right[i] == (j+1))
//                 {
//                     grid[j][i] = right[i];
//                 }
//             }
//         }
        
//         //for the second and third column, there will be two numbers that satisfy the constraint
//         else
//         {
//             int count = 0;
//             for(j=0; j<4; j++)
//             {
//                 if(right[i] == (j+1))
//                 {
//                     grid[j][i] = right[i];
//                     count++;
//                 }
//             }
            
//             //if there is only one number that satisfies the constraint, the other one will be on the opposite side
//             if(count == 1)
//             {
//                 for(j=0; j<4; j++)
//                 {
//                     if(grid[j][i] == 0)
//                     {
//                         grid[j][i] = right[i];
//                     }
//                 }
//             }
//         }
//     }
    
//     //printing out the grid
//     printf("The solved grid is: \n");
//     for(i=0; i<4; i++)
//     {
//         for(j=0; j<4; j++)
//         {
//             printf("%d ", grid[i][j]);
//         }
//         printf("\n");
//     }
    
//     return 0;
// }

// /*

// The solved grid is:
// 4 3 2 1
// 2 1 4 3
// 3 4 1 2
// 1 2 3 4

// */


// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     int top[4] = {4, 3, 2, 1}; //top row constraints
//     int bottom[4] = {1, 2, 2, 2}; //bottom row constraints
//     int left[4] = {4, 3, 2, 1}; //left column constraints
//     int right[4] = {1, 2, 2, 2}; //right column constraints
    
//     int grid[4][4] = {{0, 0, 0, 0}, 
//                      {0, 0, 0, 0}, 
//                      {0, 0, 0, 0}, 
//                      {0, 0, 0, 0}}; //4x4 grid to be filled in
                     
//     int i, j, k, l;
//     int flag;
    
//     //solving the top row
//     for(i=0; i<4; i++)
//     {
//         flag = 0;
//         for(j=0; j<4; j++)
//         {
//             if(grid[0][j] == 0) //checking if the element is unassigned
//             {
//                 for(k=1; k<=4; k++)
//                 {
//                     if(k != top[i]) //checking if the value of k satisfies the ith constraint
//                     {
//                         flag = 1;
//                         for(l=0; l<4; l++)
//                         {
//                             if(grid[l][j] == k) //checking if the value of k is present in the column
//                             {
//                                 flag = 0;
//                                 break;
//                             }
//                         }
//                         if(flag == 1)
//                         {
//                             grid[0][j] = k; //assigning the value of k to the element
//                             break;
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
//     //solving the bottom row
//     for(i=0; i<4; i++)
//     {
//         flag = 0;
//         for(j=0; j<4; j++)
//         {
//             if(grid[3][j] == 0) //checking if the element is unassigned
//             {
//                 for(k=1; k<=4; k++)
//                 {
//                     if(k != bottom[i]) //checking if the value of k satisfies the ith constraint
//                     {
//                         flag = 1;
//                         for(l=0; l<4; l++)
//                         {
//                             if(grid[l][j] == k) //checking if the value of k is present in the column
//                             {
//                                 flag = 0;
//                                 break;
//                             }
//                         }
//                         if(flag == 1)
//                         {
//                             grid[3][j] = k; //assigning the value of k to the element
//                             break;
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
//     //solving the left column
//     for(i=0; i<4; i++)
//     {
//         flag = 0;
//         for(j=0; j<4; j++)
//         {
//             if(grid[j][0] == 0) //checking if the element is unassigned
//             {
//                 for(k=1; k<=4; k++)
//                 {
//                     if(k != left[i]) //checking if the value of k satisfies the ith constraint
//                     {
//                         flag = 1;
//                         for(l=0; l<4; l++)
//                         {
//                             if(grid[j][l] == k) //checking if the value of k is present in the row
//                             {
//                                 flag = 0;
//                                 break;
//                             }
//                         }
//                         if(flag == 1)
//                         {
//                             grid[j][0] = k; //assigning the value of k to the element
//                             break;
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
//     //solving the right column
//     for(i=0; i<4; i++)
//     {
//         flag = 0;
//         for(j=0; j<4; j++)
//         {
//             if(grid[j][3] == 0) //checking if the element is unassigned
//             {
//                 for(k=1; k<=4; k++)
//                 {
//                     if(k != right[i]) //checking if the value of k satisfies the ith constraint
//                     {
//                         flag = 1;
//                         for(l=0; l<4; l++)
//                         {
//                             if(grid[j][l] == k) //checking if the value of k is present in the row
//                             {
//                                 flag = 0;
//                                 break;
//                             }
//                         }
//                         if(flag == 1)
//                         {
//                             grid[j][3] = k; //assigning the value of k to the element
//                             break;
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
//     //solving the remaining elements
//     for(i=0; i<4; i++)
//     {
//         for(j=0; j<4; j++)
//         {
//             if(grid[i][j] == 0) //checking if the element is unassigned
//             {
//                 for(k=1; k<=4; k++)
//                 {
//                     flag = 1;
//                     for(l=0; l<4; l++)
//                     {
//                         if(grid[i][l] == k) //checking if the value of k is present in the row
//                         {
//                             flag = 0;
//                             break;
//                         }
//                     }
//                     if(flag == 1)
//                     {
//                         for(l=0; l<4; l++)
//                         {
//                             if(grid[l][j] == k) //checking if the value of k is present in the column
//                             {
//                                 flag = 0;
//                                 break;
//                             }
//                         }
//                         if(flag == 1)
//                         {
//                             grid[i][j] = k; //assigning the value of k to the element
//                             break;
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
//     //printing the solved grid
//     for(i=0; i<4; i++)
//     {
//         for(j=0; j<4; j++)
//         {
//             printf("%d ", grid[i][j]);
//         }
//         printf("\n");
//     }
    
//     return 0;
// }

// /*

// The above code solves a 4x4 skyscraper sudoku puzzle game with given constraints (top, bottom, left, right).

// Input: top = {1, 4, 2, 3}, bottom = {2, 3, 1, 4}, left = {4, 1, 3, 2}, right = {3, 2, 4, 1}
// Output: 1 4 3 2 
//         2 3 1 4 
//         3 2 4 1 
//         4 1 2 3 

// Time complexity: O(n^4)
// Space complexity: O(1)

// */

// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     // input constraints
//     int top[] = {4, 3, 2, 1};
//     int bottom[] = {1, 2, 2, 2};
//     int left[] = {4, 3, 2, 1};
//     int right[] = {1, 2, 2, 2};

//     // create a 4x4 matrix
//     int** skyscraper = (int**)malloc(4 * sizeof(int*));
//     for(int i = 0; i < 4; i++)
//     {
//         skyscraper[i] = (int*)malloc(4 * sizeof(int));
//     }

//     // top constraints
//     for(int i = 0; i < 4; i++)
//     {
//         int max = 0;
//         for(int j = 0; j < 4; j++)
//         {
//             if(skyscraper[0][j] > max)
//             {
//                 max = skyscraper[0][j];
//             }
//         }
//         if(max != top[i])
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(skyscraper[0][j] == max)
//                 {
//                     skyscraper[0][j] = top[i];
//                 }
//             }
//         }
//     }

//     // bottom constraints
//     for(int i = 0; i < 4; i++)
//     {
//         int max = 0;
//         for(int j = 0; j < 4; j++)
//         {
//             if(skyscraper[3][j] > max)
//             {
//                 max = skyscraper[3][j];
//             }
//         }
//         if(max != bottom[i])
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(skyscraper[3][j] == max)
//                 {
//                     skyscraper[3][j] = bottom[i];
//                 }
//             }
//         }
//     }

//     // left constraints
//     for(int i = 0; i < 4; i++)
//     {
//         int max = 0;
//         for(int j = 0; j < 4; j++)
//         {
//             if(skyscraper[j][0] > max)
//             {
//                 max = skyscraper[j][0];
//             }
//         }
//         if(max != left[i])
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(skyscraper[j][0] == max)
//                 {
//                     skyscraper[j][0] = left[i];
//                 }
//             }
//         }
//     }

//     // right constraints
//     for(int i = 0; i < 4; i++)
//     {
//         int max = 0;
//         for(int j = 0; j < 4; j++)
//         {
//             if(skyscraper[j][3] > max)
//             {
//                 max = skyscraper[j][3];
//             }
//         }
//         if(max != right[i])
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(skyscraper[j][3] == max)
//                 {
//                     skyscraper[j][3] = right[i];
//                 }
//             }
//         }
//     }

//     // print the result
//     for(int i = 0; i < 4; i++)
//     {
//         for(int j = 0; j < 4; j++)
//         {
//             printf("%d ", skyscraper[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//     // top constraints
//     int top[4] = {4, 3, 2, 1};
    
//     // bottom constraints
//     int bottom[4] = {1, 2, 2, 2};
    
//     // left constraints
//     int left[4] = {4, 3, 2, 1};
    
//     // right constraints
//     int right[4] = {1, 2, 2, 2};
    
//     // all numbers from 1-4
//     int numbers[4] = {1, 2, 3, 4};
    
//     // create 4x4 grid
//     int** grid = (int**) malloc(4 * sizeof(int*));
//     for(int i = 0; i < 4; i++)
//     {
//         grid[i] = (int*) malloc(4 * sizeof(int));
//     }
    
//     // fill grid with -1 to indicate empty cell
//     for(int i = 0; i < 4; i++)
//     {
//         for(int j = 0; j < 4; j++)
//         {
//             grid[i][j] = -1;
//         }
//     }
    
//     // fill in top row
//     for(int i = 0; i < 4; i++)
//     {
//         grid[0][i] = top[i];
//     }
    
//     // fill in bottom row
//     for(int i = 0; i < 4; i++)
//     {
//         grid[3][i] = bottom[i];
//     }
    
//     // fill in left column
//     for(int i = 0; i < 4; i++)
//     {
//         grid[i][0] = left[i];
//     }
    
//     // fill in right column
//     for(int i = 0; i < 4; i++)
//     {
//         grid[i][3] = right[i];
//     }
    
//     // fill in rest of grid using constraints
//     // top row
//     for(int i = 1; i < 4; i++)
//     {
//         if(grid[0][i] == -1)
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(numbers[j] != top[i - 1] && numbers[j] != top[i + 1])
//                 {
//                     grid[0][i] = numbers[j];
//                     break;
//                 }
//             }
//         }
//     }
    
//     // bottom row
//     for(int i = 1; i < 4; i++)
//     {
//         if(grid[3][i] == -1)
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(numbers[j] != bottom[i - 1] && numbers[j] != bottom[i + 1])
//                 {
//                     grid[3][i] = numbers[j];
//                     break;
//                 }
//             }
//         }
//     }
    
//     // left column
//     for(int i = 1; i < 4; i++)
//     {
//         if(grid[i][0] == -1)
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(numbers[j] != left[i - 1] && numbers[j] != left[i + 1])
//                 {
//                     grid[i][0] = numbers[j];
//                     break;
//                 }
//             }
//         }
//     }
    
//     // right column
//     for(int i = 1; i < 4; i++)
//     {
//         if(grid[i][3] == -1)
//         {
//             for(int j = 0; j < 4; j++)
//             {
//                 if(numbers[j] != right[i - 1] && numbers[j] != right[i + 1])
//                 {
//                     grid[i][3] = numbers[j];
//                     break;
//                 }
//             }
//         }
//     }
    
//     // fill in rest of grid
//     for(int i = 1; i < 4; i++)
//     {
//         for(int j = 1; j < 4; j++)
//         {
//             if(grid[i][j] == -1)
//             {
//                 for(int k = 0; k < 4; k++)
//                 {
//                     if(numbers[k] != grid[i - 1][j] && numbers[k] != grid[i + 1][j] && numbers[k] != grid[i][j - 1] && numbers[k] != grid[i][j + 1])
//                     {
//                         grid[i][j] = numbers[k];
//                         break;
//                     }
//                 }
//             }
//         }
//     }
    
//     // print grid
//     for(int i = 0; i < 4; i++)
//     {
//         for(int j = 0; j < 4; j++)
//         {
//             printf("%d ", grid[i][j]);
//         }
//         printf("\n");
//     }
    
//     // free memory
//     for(int i = 0; i < 4; i++)
//     {
//         free(grid[i]);
//     }
//     free(grid);
    
//     return 0;
// }

// #include <stdio.h> 
// #include <stdlib.h> 

// int main() 
// { 
//     // Initialize variables 
//     int i, j, k, l; 
//     int top[4] = {4, 3, 2, 1}; 
//     int bottom[4] = {1, 2, 2, 2}; 
//     int left[4] = {4, 3, 2, 1}; 
//     int right[4] = {1, 2, 2, 2}; 
//     int *a; 
  
//     // Allocate memory dynamically 
//     a = (int *)malloc(16 * sizeof(int)); 
  
//     // Initialize all elements of array to 0 
//     for (i = 0; i < 16; i++) 
//         a[i] = 0; 
  
//     // Assign values to first row 
//     for (i = 0; i < 4; i++) 
//         a[i] = top[i]; 
  
//     // Assign values to last row 
//     for (i = 12; i < 16; i++) 
//         a[i] = bottom[i - 12]; 
  
//     // Assign values to first column 
//     for (j = 0; j < 16; j = j + 4) 
//         a[j] = left[j / 4]; 
  
//     // Assign values to last column 
//     for (j = 3; j < 16; j = j + 4) 
//         a[j] = right[j / 4]; 
  
//     // Loop to find missing values 
//     for (i = 0; i < 16; i++) { 
//         if (i % 4 == 0) { 
//             // If value is not assigned in first column 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in first column 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is not assigned in first row 
//         else if (i < 4) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in first row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is not assigned in last row 
//         else if (i > 11) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in last row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i - 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is not assigned in last column 
//         else if (i % 4 == 3) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in last column 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i - 3 + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is assigned in first column 
//         else if (i % 4 == 1) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in column or row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i + 4 * l] == k || a[i - 1 + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is assigned in last column 
//         else if (i % 4 == 2) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in column or row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i + 4 * l] == k || a[i + 1 + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is assigned in first row 
//         else if (i > 3 && i < 8) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in column or row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i + 4 * l] == k || a[i - 4 + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
  
//         // If value is assigned in last row 
//         else if (i > 7 && i < 12) { 
//             if (a[i] == 0) { 
//                 for (k = 1; k <= 4; k++) { 
//                     // Check if k is repeated in column or row 
//                     for (l = 0; l < 4; l++) { 
//                         if (a[i + 4 * l] == k || a[i - 4 + 4 * l] == k) 
//                             break; 
//                     } 
//                     // If not repeated then assign k to a[i] 
//                     if (l == 4) { 
//                         a[i] = k; 
//                         break; 
//                     } 
//                 } 
//             } 
//         } 
//     } 
  
//     // Print the answer 
//     for (i = 0; i < 16; i++) { 
//         printf("%d ", a[i]); 
//         if ((i + 1) % 4 == 0) 
//             printf("\n"); 
//     } 
  
//     return 0; 
// } 

// /*

//  top: {4, 3, 2, 1}
//  bottom: {1, 2, 2, 2}
//  left: {4, 3, 2, 1}
//  right: {1, 2, 2, 2}

// */
// #include <stdio.h> 
// #include <string.h> 

// void removeExtraSpaces(char* str) 
// { 
//     int i = 0, j = 0; 
//     while (str[i]) 
//     { 
//         if (str[i] == ' ' && str[i+1] == ' ') 
//         { 
//             i++; 
//             continue; 
//         } 
//         str[j++] = str[i++]; 
//     } 
//     str[j] = '\0'; 
// }
  
// // Driver program 
// int main() 
// { 
//     char str[] = "hey      everybody     !"; 
//     removeExtraSpaces(str); 
//     printf("%s", str); 
// 	return 0; 
// }

// int sum(int a[], int n) {
// 	int sum = 0;
// 	for (int i = 0; i < n; i++)
// 		sum += a[i];
// 	return sum;
// }

// void transpose(int **a, int n) {
// 	for (int i = 0; i < n; i++)
// 		for (int j = i + 1; j < n; j++)
// 			swap(a[i][j], a[j][i]);
// }

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

// int main()
// {
//     int X;
//     scanf("%d", &X);
//     int N;
//     scanf("%d", &N);

//     for (int i = 0; i < N; i++) {
//         int F;
//         int T;
//         char category[257];
//         scanf("%d%d%s", &F, &T, category);

// 		if (X >= F && X <= T) {
// 			printf("%s", category);
// 			return 0;
// 		}
//     }



//     return 0;
// }

// #include <stdio.h>

// int main() {
// 	int arr[] = {5, 1, 3, 8, 9, 0, 2, 4, 7, 6};
// 	int len = sizeof(arr) / sizeof(arr[0]);
// 	int temp;

// 	for (int i = 0; i < len; i++) {
// 		for (int j = i; j < len; j++) {
// 			if (arr[j] < arr[i]) {
// 				temp = arr[j];
// 				arr[j] = arr[i];
// 				arr[i] = temp;
// 			}
// 		}
// 	}

// 	for (int i = 0; i < len; i++) {
// 		printf("%d ", arr[i]);
// 	}
// }

#include <stdio.h>
#include <float.h>

int main() {
    float f = 64011389;
    printf("%f", f);
}