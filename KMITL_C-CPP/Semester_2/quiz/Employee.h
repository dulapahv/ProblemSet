#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <string>

using namespace std;

class Employee {
protected:
    string name;
    int age;
    double basic_salary;
public:
    /** Employee - Constructor taking name, age and basic salary **/
    Employee(string name, int age, double basic_salary) {
        this->name = name;
        this->age = age;
        this->basic_salary = basic_salary;
    };

    virtual double calcSalary();
    virtual void print();
};

#endif  // EMPLOYEE_H