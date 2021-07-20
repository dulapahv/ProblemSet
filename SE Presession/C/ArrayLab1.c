#include <stdio.h>

int main(){
    int cases; // delcare int cases
    scanf("%d", &cases);  // input cases
    int sol[cases]; // declare an array with the size of cases
    for(int i=0; i < cases; i++){ // loop each case
        int amount, usin, sum=0; // amount = loop input, usin=input value sum
        scanf("%d", &amount); // input data set size
        for(int j=0; j < amount; j++){ // loop input data set
            scanf("%d", &usin); // input usin
            sum += usin; // add to sum
        }
        sol[i] = sum;
    }
    for(int i=0; i < cases; i++){
        printf("%d\n", sol[i]);
    }
}