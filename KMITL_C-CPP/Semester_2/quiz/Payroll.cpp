#include "assert.h"
#include "Payroll.h"

bool Payroll::addEmployee(Employee* e) {
    assert(e != NULL);
    employee_reg.push_back(e);
	return 1;
}

double Payroll::calcTotalWages() {
    double sum = 0.0;

	for (int j = 0; j < employee_reg.size(); j++) {
		sum += employee_reg[j]->calcSalary();
	}

	fprintf(stderr, "Total wages: %10.2f\n", sum);
	return (sum);
}

void Payroll::print() {
    fprintf(stdout, "Employee Register\n");

	for (int j = 0; j < employee_reg.size(); j++) {
		employee_reg[j]->print();
	}
}