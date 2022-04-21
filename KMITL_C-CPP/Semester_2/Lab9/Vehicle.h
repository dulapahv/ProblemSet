#pragma once

#include <string>

using namespace std;

class Vehicle {
protected:
    string name;
    double cost;
    int year;
public:
    Vehicle();

    Vehicle(string name, double cost, int year) {
        this->name = name;
        this->cost = cost;
        this->year = year;
    }

    void setName(string name);
    string getName();

    void setCost(double cost);
    double getCost();
    
    void setYear(int year);
    int getYear();
    
    void print();
};
