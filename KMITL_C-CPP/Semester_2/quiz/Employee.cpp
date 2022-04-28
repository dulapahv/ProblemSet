#include <iostream>

#include "Employee.h"

using namespace std;

double Mechanic::calcSalary() {
    return basic_salary * multiplier;
}

void Mechanic::print() {
    cout << "Mechanic: " << name << " " << age << " " << basic_salary << " " << multiplier << endl;
}

/**/

double Engineer::calcSalary() {
    return basic_salary * multiplier;
}

void Engineer::print() {
    cout << "Engineer: " << name << " " << age << " " << basic_salary << " " << multiplier << endl;
}

/**/

double SecurityGuard::calcSalary() {
    return basic_salary * multiplier;
}

void SecurityGuard::print() {
    cout << "Security Guard: " << name << " " << age << " " << basic_salary << " " << multiplier << endl;
}

/**/

double TeaServer::calcSalary() {
    return basic_salary * multiplier;
}

void TeaServer::print() {
    cout << "Tea Server: " << name << " " << age << " " << basic_salary << " " << multiplier << endl;
}