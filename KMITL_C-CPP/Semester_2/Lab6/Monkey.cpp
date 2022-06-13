// Monkey.cpp : Monkey class
//

#include <cstdio>
#define _USE_MATH_DEFINES
#include <cmath>

#include "Monkey.h"

// Av length of verterbrae 
double m_v_length = 0.35;
// string m_z_name("Cercopithecidae");
const string m_z_name("Cercopithecidae");

Monkey::Monkey() {
    printM();
}

/* Get length of the skeleton */
double Monkey::getLength() {
    double s_len = getNVert() * m_v_length;
    return s_len;
}

void Monkey::printM() {
    fprintf(stdout, "Monkey: %s (%s)\n",
        getCommonName().c_str(), getZooName().c_str());
    fprintf(stdout, "Verterbrae %d Toes %d\n", getNVert(), getNToes());
}