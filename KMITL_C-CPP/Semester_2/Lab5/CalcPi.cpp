// CalcPi.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

#include "Rectangle.h"
#include "Complex.h"
#include "Pt.h"
#include <iomanip>
#include <vector> // for vectors

#include "DivideByZeroException.h"
#include "OverflowException.h"

using namespace std;

const int n_max = 10000;

/** Generate a random point in (0,0) - (1,1) */
Pt<double> randomPt() {
	Pt<double> p;
	p.x = (double)rand() / (double)RAND_MAX;
	p.y = (double)rand() / (double)RAND_MAX;
	return p;
}

/* Is p inside the unit circle? - if outside, throw an exception */
bool inside(Pt<double> p) {
	double distance = sqrt((p.x * p.x) + (p.y * p.y));
	if (distance <= 1)
		return true;
	else
		throw OverflowException();
}

double pi_est(int n_in, int n_tot) {
	return 4.0 * (double)n_in / (double)n_tot;
}

const int max_tries = 10000000; /* Set as large as you like */

int main() {
	vector<double> pi_calcs;
	vector<int> n_trials;
	Pt<double> p;
	int n_inside, n_total, n_report;
	double pi_v;
	fprintf(stderr, "Calculate pi\n");
	/* Random seed */
	srand((unsigned int)time(0));
	n_inside = 0;
	n_total = 200;
	n_report = 100; /* Report at regular intervals */
	for (int j = 0; j < max_tries; j++) {
		p = randomPt();
		n_total++;
		/** Add a try-catch block */
		try {
			if (inside(p))
				n_inside += 1;
		}
		catch (OverflowException& overflowException) {}
		/************ count n_inside and n_total ***************************/
		if (n_total > n_report) {
			pi_v = pi_est(n_inside, n_total);
			fprintf(stderr, "Tries %d pi %20.12f err %10.4g %%\n",
				n_total, pi_v, 100.0 * (M_PI - pi_v) / M_PI);
			n_report = n_report * 3 / 2; /* Increment the reporting interval */
			pi_calcs.push_back(pi_v);
			n_trials.push_back(n_total);
		}
	}

	/* Print a summary of your trials */
	/*****************************/
	cout << "Attempt No.\t\t Value" << endl;
	for (int i = 0; i < pi_calcs.size(); i++)
		cout << n_trials[i] << "\t\t" << setprecision(12) << fixed << pi_calcs[i] << endl;
	
	return 0;
}