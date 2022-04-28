#ifndef MECHANIC_H
#define MECHANIC

#include "Employee.h"

#include <string>
#include <vector>

using namespace std;

class Mechanic : public Employee {
protected:
    vector<string> flags;
public:
    /** Mechanic - Constructor taking name, age, basic salary and flags **/
    Mechanic(string name, int age, double basic_salary, vector<string> flags) : Employee(name, age, basic_salary) {
        this->flags = flags;
    };

    double calcSalary();
};

#endif  // MECHANIC