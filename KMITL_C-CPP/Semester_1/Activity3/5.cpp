/* Pseudocode */
// Get character from a file
// Convert to lower case
// Print out the converted character
// Output to another file

#include <stdio.h>
#include <string>

int main() {
    FILE* in_file = fopen("5_in.txt", "r");
    FILE* out_file = fopen("5_out.txt", "w");
    for (int c; (c = fgetc(in_file)) != EOF;)
        fprintf(out_file, "%c", tolower(c));
    fclose(in_file);
    fclose(out_file);
}