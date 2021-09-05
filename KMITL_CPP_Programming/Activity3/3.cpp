/* Pseudocode */
// Get character from a file
// Check if character is blank. If so, check whether previous character is not blank. If so, print out the character itself
// But if the character is not blank, print out the character itself
// Store the previous character in the variable to be checked next time
// Output to another file

#include <stdio.h>

int main() {
    FILE* in_file = fopen("3_in.txt", "r");
    FILE* out_file = fopen("3_out.txt", "w");
    for (int c, cEnd; (c = fgetc(in_file)) != EOF;) {
        if (c == ' ') {
            if (cEnd != ' ')
            fprintf(out_file, "%c", c);
        }
        else
            fprintf(out_file, "%c", c);
        cEnd = c;
    }
    fclose(in_file);
    fclose(out_file);
}