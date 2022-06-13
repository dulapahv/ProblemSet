#include <stdio.h>
#include <string.h>

int main(){
    char input[51];
    int c=0, g=0, t=0; // amount of type of cards
    scanf("%s", input); // card input
    for(int i=0; i<strlen(input); i++){ // card input
        if(input[i] == 'C') // check
            c++;
        else if(input[i] == 'G')
            g++;
        else if(input[i] == 'T')
            t++;
    }
    int score = ((c*c) + (g*g) + (t*t));
    if(c != 0 && g != 0 && t != 0){
        int min = c; 
        if(g < min)
            min = g;
        if (t < min)
            min = t;
        score += (min * 7);
    }
    printf("%d",score);
}
