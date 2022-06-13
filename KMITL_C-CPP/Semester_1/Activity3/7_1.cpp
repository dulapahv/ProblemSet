/* Pseudocode */
// 1. get the number of line in file
// while end of file is not reached
//      execute a function to get the length of each line input file
//          length + 1 as long as it's not the end of line
//          add null terminator (\0) after reading all line
//          if c == EOF, returns EOF (-1), otherwise returns length of each line
//      if len is end of file (-1), break out of loop
//      if length of line is invalid, return "invalid input"
//      if length of line is valid (> 0)
//          recount length excluding ' ', '\t', '\n', '\r'
//      set buffer to the start of line (at 0)
//
// 2. get the number of value in each line
// let cur = buffer, loop as long as cur is not null (0) while also assigning cur = end
//      convert cur to double and store in val. If unconvertible, store in end
//      if somehow cur == end, return error
//
// 3. get the sum of current number and previous number and write them into the file
// result = result + sum of all previous number. Which is result += val
// store them into the file

#include <iostream>

#define BUFFER_SIZE 81

int get_line(FILE *fp, char *buffer, int size) { // returns the length of each line in input file, including escape sequence and returns -1 for end of file
    char *end = buffer + size, *dst = buffer;
    int c;
    while ((c = fgetc(fp)) != EOF && c != '\n' && dst <= end) { // loop as long as it's not end of line
        *dst = c;
        dst++;
    }
    *dst = '\0'; // add null terminator (\0) after reading all line
    return ((c == EOF && dst == buffer) ? EOF : dst - buffer); // if c == EOF, returns EOF (-1), otherwise returns length of each line
}

int main() {
    FILE *in_file = fopen("7_1in.txt", "rb");
    FILE *out_file = fopen("7_1out.txt", "wb");
    char *cur, *end, buffer[BUFFER_SIZE];
    for (int len; !feof(in_file);) { // while end of file is not reached
        len = get_line(in_file, buffer, BUFFER_SIZE);
        if (len == -1) // if len is end of file (-1), break out of loop
            break;
        if ((len < 1) || (buffer[len - 1] != '\r')) { // if length of line is invalid, return "invalid input"
            fprintf(stderr, "invalid input");
            return -1;
        }
        while (len > 0) { // if length of line is valid
            --len;
            if (buffer[len] != ' ' && buffer[len] != '\t' && buffer[len] != '\n' && buffer[len] != '\r') { // recount length excluding these characters
                ++len;
                break;
            }
        }
        buffer[len] = 0; // set buffer to the start of line (at 0)

        double val, partSum;
        for (cur = buffer; *cur != 0; cur = end) { // let cur = buffer, loop as long as cur is not null (0) while also assigning cur = end
            val = strtod(cur, &end); // convert cur to double and store in val. If unconvertible, store in end
            if (cur == end) { // if somehow cur == end, return error
                fprintf(stderr, "invalid");
                return -1;
            }
            partSum += val;
            fprintf(out_file, "%.6g ", partSum);
        }
    }
    fclose(in_file);
    fclose(out_file);
}