#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <iostream>
#include <string>
#include <vector>

#include "Fleet.h"
#include "EmptyVehicleException.h"

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

    virtual double calcSalary() { return basic_salary; }
    virtual void print() {};
};


class Engineer : public Employee {
protected:
    double multiplier = 1.5;
public:
    /** Engineer - Constructor taking name, age, basic salary and multiplier **/
    Engineer(string name, int age, double basic_salary) : Employee(name, age, basic_salary) {};

    double calcSalary();
    void print();
};


class Mechanic : public Employee {
protected:
    vector<Vehicle> flags;
    double multiplier;
public:
    /** Mechanic - Constructor taking name, age, basic salary and flags **/
    Mechanic(string name, int age, double basic_salary, vector<Vehicle> flags) : Employee(name, age, basic_salary) {
        this->flags = flags;
        if (flags.size() != 0) {
            multiplier = 1 + (flags.size() / 10.0);
        }
        else {
            throw EmptyVehicleException();
        }
    };

    double calcSalary();
    void print();
};


class TeaServer : public Employee {
protected:
    double multiplier = 1.0;
public:
    /** TeaServer - Constructor taking name, age, basic salary and multiplier **/
    TeaServer(string name, int age, double basic_salary) : Employee(name, age, basic_salary) {};

    double calcSalary();
    void print();
};


class SecurityGuard : public Employee {
protected:
    double multiplier = 1.2;
public:
    /** SecurityGuard - Constructor taking name, age, basic salary and multiplier **/
    SecurityGuard(string name, int age, double basic_salary) : Employee(name, age, basic_salary) {};

    double calcSalary();
    void print();
};


#endif  // EMPLOYEE_H