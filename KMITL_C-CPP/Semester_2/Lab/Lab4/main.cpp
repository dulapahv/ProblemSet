#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include "Region.h"

#define INPUT "input.txt"
#define OUTPUT "output.txt"

using namespace std;

int main() {
    /* Reads input file */
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
        if (strcmp(type, "Province") == 0)
            province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
        else if (strcmp(type, "Sub") == 0)
            sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
        else if (strcmp(type, "Town") == 0)
            town.push_back(Town(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
    }
    
    /** DEBUG **/
    /* Get name of each province and sub-district */
    cout << "\nProvince:" << endl;
    for (int i = 0; i < province.size(); i++)
        cout << province[i].getName() << endl;
    cout << "\nSub-District:" << endl;
    for (int i = 0; i < sub_district.size(); i++)
        cout << sub_district[i].getName() << endl;
    for (int i = 0; i < town.size(); i++)
        cout << town[i].getName() << endl;
    
    /* Get sum of population in each province */
    double sumProvince = 0, sumSub = 0, sumTown = 0;
    for (int i = 0; i < province.size(); i++)
        sumProvince += province[i].getPopulation();
    for (int i = 0; i < sub_district.size(); i++)
        sumSub += sub_district[i].getPopulation();
    for (int i = 0; i < town.size(); i++)
        sumTown += town[i].getPopulation();

    cout << setprecision(12) << "\nSum Province: " << sumProvince << endl;
    cout << "Sum Sub-District: " << sumSub << endl;
    cout << "Sum Town: " << sumTown << endl;

    /* Get area of each province */
    double sumProvinceArea = 0, sumSubArea = 0, sumTownArea = 0;
    for (int i = 0; i < province.size(); i++)
        sumProvinceArea += province[i].getArea();
    for (int i = 0; i < sub_district.size(); i++)
        sumSubArea += sub_district[i].getArea();
    for (int i = 0; i < town.size(); i++)
        sumTownArea += town[i].getArea();
    
    cout << "\nProvince Area: " << sumProvinceArea << endl;
    cout << "Sub-District Area: " << sumSubArea << endl;
    cout << "Sum Town Area: " << sumTownArea << endl;

    /* Get population density of each province and sub-district */
    cout << "\nProvince population density:" << endl;
    for (int i = 0; i < province.size(); i++)
        cout << province[i].getName() << ": " << province[i].getPopulationDensity() << endl;
    cout << "\nSub-District population density:" << endl;
    for (int i = 0; i < sub_district.size(); i++)
        cout << sub_district[i].getName() << ": " << sub_district[i].getPopulationDensity() << endl;
    for (int i = 0; i < town.size(); i++)
        cout << town[i].getName() << ": " << town[i].getPopulationDensity() << endl;

    inFile.close();
    return 0;
}