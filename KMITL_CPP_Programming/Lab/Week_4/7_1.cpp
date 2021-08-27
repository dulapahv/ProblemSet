/* Pseudocode */
// 

#include <iostream>

#define BUFFER_SIZE 81

int get_line(FILE *fp, char *buffer, int size) { // returns the length of each line in input file, including escape sequence and returns -1 for end of file
    char *end = buffer + size, *dst = buffer;
    int c;
    while ((c = fgetc(fp)) != EOF && c != '\n' && dst <= end) { // loop as long as it's not end of line
        *dst = c;
        dst++;
    }
    *dst = '\0'; // terminate sequence
    return ((c == EOF && dst == buffer) ? EOF : dst - buffer);
}

int main() {
    FILE *in_file = fopen("7_1in.txt", "rb");
    FILE *out_file = fopen("7_1out.txt", "wb");
    char *cur, *end, buffer[BUFFER_SIZE];
    for (int len; !feof(in_file);) {
        len = get_line(in_file, buffer, BUFFER_SIZE);
        if (len == -1) // if len is end of file (-1), break out of loop
            break;
        if ((len < 1) || (buffer[len - 1] != '\r')) { // if length of line is invalid
            fprintf(stderr, "invalid input");
            return -1;
        }
        while (len > 0) {
            --len;
            if (buffer[len] != ' ' && buffer[len] != '\t' && buffer[len] != '\n' && buffer[len] != '\r') {
                ++len;
                break;
            }
        }
        buffer[len] = 0;

        double val, partSum;
        for (cur = buffer; *cur != 0; cur = end) {
            val = strtod(cur, &end);
            if (cur == end) {
                fprintf(stderr, "invalid");
                return -1;
            }
            partSum += val;
            fprintf(out_file, "%.6g ", partSum);
        }
    }
}