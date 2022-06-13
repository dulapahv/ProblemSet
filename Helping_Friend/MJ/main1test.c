#include <stdio.h>

int main() {
    FILE*input = fopen("beforetest.txt", "r");
    int bd=1;
    if (input == NULL)
    {
        input = fopen("beforetest.txt", "w");
        for(int i=1;i<=20;i++) {
            if (i == 1)
                fprintf(input, "morning\n");
            else if (i == 11)
                fprintf(input, "\nevening\n");
            fprintf(input, "%d.\n", bd);
            for (int j = 1; j <= 50; j++) {
                if (j % 5 == 0) {
                    fprintf(input, "empty\n");
                }
                else {
                    fprintf(input, "empty ");
                }
            }
            bd++;
            if (bd == 11)
                bd = 1;
        }
    }
}
