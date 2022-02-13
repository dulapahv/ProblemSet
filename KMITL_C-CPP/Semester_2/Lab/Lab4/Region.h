#pragma once

#include <string>

using namespace std;

class Region {
private:
	string key;
	string name;
	double latitude = 0.0, longitude = 0.0;
	double population = 0;
	double area = 0.0;
public:
	Region();
	Region(string key, string name, double latitude, double longitude, double population, double area);
	string getKey();
	string getName();
	double getLatitude();
	double getLongitude();
	double getPopulation();
	double getArea();
	double getPopulationDensity();
};