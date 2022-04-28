#ifndef TEASERVER_H
#define TEASERVER_H

#include "Employee.h"

class TeaServer : public Employee {
protected:
    double multiplier = 1;
public:
    /** TeaServer - Constructor taking name, age, basic salary and multiplier **/
    TeaServer(string name, int age, double basic_salary, double multiplier) : Employee(name, age, basic_salary) {
        this->multiplier = 1;
    }

    double calcSalary();
};

#endif  // TEASERVER_H