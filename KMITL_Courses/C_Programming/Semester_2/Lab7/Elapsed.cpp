
#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <Sysinfoapi.h>
#include "Elapsed.h"

static double last_time = 0.0;
double elapsed() {
    double t = (double)GetTickCount();
    //fprintf(stderr, "curr %10.6f last %10.6f\n", t, last_time);
    double el = t - last_time;
    last_time = t;
    //fprintf(stderr, "el %10.6f\n", el);
    return el / 1000.0;
}
