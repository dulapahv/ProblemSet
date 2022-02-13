#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "Region.h"

#define INPUT "input.txt"
#define OUTPUT "output.txt"

using namespace std;

int main() {
    /** Reads input file **/
    ifstream inFile(INPUT);

    vector<Region> region;
    vector<Province> province;
    vector<Sub_District> sub_district;
    vector<Town> town;

    /* Move file pointer to the next line */
    inFile.ignore(256, '\n');

    /* Store read data in vector */
    string tempKey, tempName;
    double tempLatitude, tempLongitude, tempPopulation, tempArea;
    while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {
        /* Store data according to the region type */
        const char * type = tempKey.c_str(); // Convert string to const char *
        if (strcmp(type, "Province"))
            province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
        else if (strcmp(type, "Sub_District"))
            sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
        else if (strcmp(type, "Town")) {
            town.push_back(Town(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
    }

    inFile.close();
    return 0;
}