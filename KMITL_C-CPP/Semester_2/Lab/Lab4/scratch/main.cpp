#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define INPUT "C:\\Users\\Dulapah Vibulsanti\\OneDrive - KMITL\\Documents\\GitHub\\ProblemSet\\KMITL_C-CPP\\Semester_2\\Lab\\Lab4\\scratch\\input.txt"
#define OUTPUT "C:\\Users\\Dulapah Vibulsanti\\OneDrive - KMITL\\Documents\\GitHub\\ProblemSet\\KMITL_C-CPP\\Semester_2\\Lab\\Lab4\\scratch\\output.txt"

using namespace std;

int main() {
    /** Reads input file **/
    ifstream inFile(INPUT);
    vector<string> key, name;
    vector<double> latitude, longitude, population, area;
    
    /* Move file pointer to the next line */
    inFile.ignore(256, '\n');

    /* Store read data in variables*/
    // Store read data in temporary variables before storing in vectors
    string tempKey, tempName;
    double tempLatitude, tempLongitude, tempPopulation, tempArea;
    while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {
        key.push_back(tempKey);
        name.push_back(tempName);
        latitude.push_back(tempLatitude);
        longitude.push_back(tempLongitude);
        population.push_back(tempPopulation);
        area.push_back(tempArea);
        cout << tempArea << " " << tempLatitude << " " << tempLongitude << " " << tempPopulation << " " << tempName << " " << tempKey << endl;
    }

    inFile.close();
    return 0;
}