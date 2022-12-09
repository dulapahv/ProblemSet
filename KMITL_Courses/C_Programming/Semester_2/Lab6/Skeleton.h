// Skeleton.h : Skeleton
//

#pragma once

#include <cstdio>
#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>

using namespace std;

class Skeleton {
private:
    int n_vert;
    int n_toes;

public:
    Skeleton();
    Skeleton(int n_vert, int n_toes);
    void setVert(int n);
    int getNVert();
    int getNToes();
    double getLength();
    void printS();
};