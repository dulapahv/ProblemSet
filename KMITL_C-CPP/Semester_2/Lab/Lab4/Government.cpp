#include "Government.h"
#include <iostream>
#include <vector>

using namespace std;

Government::Government() {
    key = "";
    name = "";
    latitude = 0.0;
    longitude = 0.0;
    population = 0;
    area = 0.0;
}

Government::Government(string key, string name, double latitude, double longitude, double population, double area) {
    this->key = key;
    this->name = name;
    this->latitude = latitude;
    this->longitude = longitude;
    this->population = population;
    this->area = area;
}

Government::~Government() {
    cout << "Removed " << this->name << "from " << this->key << endl;
}

string Government::getKey() {
    return this->key;
}

string Government::getName() {
    return this->name;
}

double Government::getLatitude() {
    return this->latitude;
}

double Government::getLongtitude() {
    return this->longitude;
}

double Government::getPopulationDensity() {
    return this->population / this->area;
}