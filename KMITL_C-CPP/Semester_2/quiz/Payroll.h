#ifndef PAYROLL_H
#define PAYROLL_H

#include <iostream>
#include <string>
#include <vector>
#include "Employee.h"

using namespace std;

class Payroll {
private:
	vector<Employee*> employee_reg;
public:
	Payroll(vector<Employee*> employees);

    bool addEmployee(Employee* employee);
	double calcTotalWages();
    void print();
};

#endif  // PAYROLL_H