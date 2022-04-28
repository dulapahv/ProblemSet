#ifndef SECURITYGUARD_H
#define SECURITYGUARD_H

#include "Employee.h"

class SecurityGuard : public Employee {
protected:
    double multiplier = 1.2;
public:
    /** SecurityGuard - Constructor taking name, age, basic salary and multiplier **/
    SecurityGuard(string name, int age, double basic_salary) : Employee(name, age, basic_salary) {};

    double calcSalary();
};

#endif  // SECURITYGUARD_H