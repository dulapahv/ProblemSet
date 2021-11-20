#include <stdio.h>
#include <string.h>
int main(){
    char answer[18], guess[27], check[18], stat[5] = "LOSE";
    int count_down=10;
    gets(answer);
    gets(guess);
    for(int i=0; i<=strlen(answer); i++){
        check[i] = '-';
        if(i == strlen(answer))
            check[i] = '\0';
    }
    for(int i=0; i<26;i++){
        if(strcmp(answer,check) == 0){
            strcpy(stat,"WIN");
            break;
        }
        if(count_down == 0)
            break;
        int flag =0;
        for(int j=0; j<strlen(answer); j++){
            if(guess[i] == answer[j]){
                answer[j] = '-';
                flag = 1;
            }
        }
        if(flag == 0)
            count_down--;
    }
    puts(stat);
}