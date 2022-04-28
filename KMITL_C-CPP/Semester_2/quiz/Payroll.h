#ifndef PAYROLL_H
#define PAYROLL_H

#include <vector>

#include "Employee.h"

class Payroll {
private: 
	vector<Employee*> employee_reg;
public: 
	Payroll() {};

	bool addEmployee(Employee* e);
	double calcTotalWages();
	void print();
};

#endif  // PAYROLL_H