#include "Region.h"

Region::Region() {}
Region::Region(string key, string name, double latitude, double longitude, long long int population, double area) {
    this->key = key;
    this->name = name;
    this->latitude = latitude;
    this->longitude = longitude;
    this->population = population;
    this->area = area;
}

string Region::getKey() { return this->key; }
string Region::getName() { return this->name; }
double Region::getLatitude() { return this->latitude; }
double Region::getLongitude() { return this->longitude; }
long long int Region::getPopulation() { return this->population; }
double Region::getArea() { return this->area; }
double Region::getPopulationDensity() { return this->population / this->area; }

Province::Province() {}
Province::Province(string key, string name, double latitude, double longitude, long long int population, double area) : Region(key, name, latitude, longitude, population, area) {}

Sub_District::Sub_District() {}
Sub_District::Sub_District(string key, string name, double latitude, double longitude, long long int population, double area) : Region(key, name, latitude, longitude, population, area) {}