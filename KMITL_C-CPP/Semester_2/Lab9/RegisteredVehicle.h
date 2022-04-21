#pragma once

#include <string>

#include "Vehicle.h"

using namespace std;

class RegisteredVehicle : public Vehicle {
private:
    string reg_no;
public:
    RegisteredVehicle();

    RegisteredVehicle(string newname, double cost, int year, string reg_no) {
        this->name = newname;
        this->cost = cost;
        this->year = year;
        this->reg_no = reg_no;
    }

    void setRegNo(string reg_no) { this->reg_no = reg_no; }
    string getRegNo() { return reg_no; }

    void print() {
        fprintf(stdout, "Name: %s\n", name.c_str());
        fprintf(stdout, "Cost: %10.2f\n", cost);
        fprintf(stdout, "Year: %d\n", year);
        fprintf(stdout, "Reg No: %s\n", reg_no.c_str());
        this->name = name;
        this->cost = cost;
        this->year = year;
    }
};
