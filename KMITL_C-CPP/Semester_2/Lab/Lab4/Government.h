#pragma once

#include <string>

using namespace std;

class Government {
private:
	string key;
	string name;
	double latitude, longitude;
	double population;
	double area;
public:
	Government();
	Government(string key, string name, double latitude, double longitude, double population, double area);
	~Government();

	string getKey();
	string getName();
	double getLatitude();
	double getLongtitude();
	double getPopulation();
	double getArea();
	double getPopulationDensity();
};

class Town : public Government {
public:
	Town();
	Town(string key, string name, double latitude, double longitude, double population, double area);
};	

class District : public Government {
private:
	vector<Town> DistrictVec;
public:
	District();
	District(string key, string name, double latitude, double longitude, double population, double area);
};

class Province : public Government {
private:
	vector<District> ProvinceVec;
public:
	Province();
	Province(string key, string name, double latitude, double longitude, double population, double area);
};