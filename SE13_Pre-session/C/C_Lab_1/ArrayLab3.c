#include <stdio.h>

int main(){
    int cases, student;
    scanf("%d", &cases); // testcases
    double sol[cases];  // arr sol
    for(int i=0; i<cases; i++){ // biggest loop
        scanf("%d", &student); //input student
        int count=0; // count the above avg
        double data[student],avg = 0;
        for(int i=0; i<student; i++){ // loop input
            scanf("%lf", &data[i]);
            avg += data[i];  // avg-> sum
        }
        avg /= student;  // avg correct
        for(int i=0; i<student; i++){ // loop to check above average
            if(data[i] > avg){
                count++;
            }
        }
        sol[i] = ((double)count/student)*100;
    }
    for(int i=0; i<cases; i++){
        printf("%.3lf%%\n",sol[i]);
    }
}
