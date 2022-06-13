#pragma once

#include <string>

using namespace std;

/* Abstract class */
class Region {
private:
	string key;
	string name;
	double latitude = 0.0, longitude = 0.0;
	long long int population = 0;
	double area = 0.0;
public:
	Region();
	Region(string key, string name, double latitude, double longitude, long long int population, double area);
	string getKey();
	string getName();
	double getLatitude();
	double getLongitude();
	long long int getPopulation();
	double getArea();
	double getPopulationDensity();
};


class Province : public Region {
public:
	Province();
	Province(string key, string name, double latitude, double longitude, long long int population, double area);
	string getProvince();
};


class Sub_District : public Region {
public:
	Sub_District();
	Sub_District(string key, string name, double latitude, double longitude, long long int population, double area);
	string getSub_District();
};