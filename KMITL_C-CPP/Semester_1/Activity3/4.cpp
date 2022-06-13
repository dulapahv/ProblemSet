/* Pseudocode */
// Get character from a file
// Check if character is backslash. If so, print out another backslash to make it appeared "\\"
// Check if character is a tab. If so, print out "\t"
// If it is neither of them, print out the character itself
// Output to another file

#include <stdio.h>

int main() {
    FILE* in_file = fopen("4_in.txt", "r");
    FILE* out_file = fopen("4_out.txt", "w");
    for (int c; (c = fgetc(in_file)) != EOF;) {
        if (c == '\\')
            fprintf(out_file, "\\");
        if (c == '\t') {
            fprintf(out_file, "\\");
            fprintf(out_file, "t");
        }
        fprintf(out_file, "%c", c);
    }
    fclose(in_file);
    fclose(out_file);
}