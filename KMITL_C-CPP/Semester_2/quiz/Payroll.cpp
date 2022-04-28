#include "Payroll.h"

bool Payroll::addEmployee(Employee* employee) {
    employee_reg.push_back(employee);
	return (1);
}

double Payroll::calcTotalWages() {
	double sum = 0.0;

	for (int j = 0; j < employee_reg.size(); j++) {
		sum += employee_reg[j]->calcSalary();
	}

	fprintf(stderr, "Total cost: %10.2f\n", sum);
	return (sum);
}

void Payroll::print() {
	fprintf(stdout, "Asset Register\n");

	for (int j = 0; j < employee_reg.size(); j++) {
		employee_reg[j]->print();
	}
}