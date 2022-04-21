#include "Vehicle.h"

void Vehicle::setName(string name) { this->name = name; }
string Vehicle::getName() { return name; }

void Vehicle::setCost(double cost) { this->cost = cost; }
double Vehicle::getCost() { return cost; }

void Vehicle::setYear(int year) { this->year = year; }
int Vehicle::getYear() { return year; }

void Vehicle::print() {
    fprintf(stdout, "Name: %s\n", name.c_str());
    fprintf(stdout, "Cost: %.2f\n", cost);
    fprintf(stdout, "Year: %d\n", year);
}