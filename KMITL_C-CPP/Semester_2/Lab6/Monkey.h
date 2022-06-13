// Monkey.h : Monkey
//

#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>

#include "Animal.h"
#include "Skeleton.h"

using namespace std;

extern const string m_z_name;

class Monkey : public Animal, public Skeleton {
private:
    int id;
    double location;

public:
    Monkey();

    Monkey(string c_name) :Animal(c_name, m_z_name), Skeleton(32, 5) {
        fprintf(stdout, "Monkey %s (%s) constructed\n", c_name.c_str(), m_z_name.c_str());
        printM();
    }

    /* Get length of the skeleton */
    double getLength();
    void printM();
};