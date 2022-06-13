#include <malloc.h>

class PressureReadings {
   double *p;
   int n_read;

   PressureReadings( int n_read ) {
      p = (double *)calloc(sizeof(double), n_read );
      }
   double calcMeanPress() {
      double *pj = p, sum = 0.0;
      for(int j=0;j<n_read;j++)sum += *pj++;
      return sum / n_read;
      }
};
