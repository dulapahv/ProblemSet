#include <stdlib.h>
#include <stdio.h>

#define LINE_BUFFER_SIZE 81

int read_line(FILE *f, char buf[], int n) {
    //n = buffer size
    if (n < 1)
        return 0; //buffer empty

    int c, i;
    for (i = 0; i < n - 1; i++) {
        if ((c = fgetc(f)) != EOF) { //get each character
            buf[i] = c;
            if (c == '\n') { //end of line
                buf[++i] = 0;
                return i;
            }
        }
        else {
            buf[++i] = '\n';
            break;
        }
    }
    buf[i] = 0;
    return i; //returns length of current line
}

int main() {
    FILE *in_file = fopen("6_1in.txt", "rb");
    FILE *out_file = fopen("6_1out.txt", "wb");
    int sum = 0;
    char line[LINE_BUFFER_SIZE];
    char *cur, *end;
    for (int len; !feof(in_file);) {
        len = read_line(in_file, line, LINE_BUFFER_SIZE);
        fprintf(stdout, "len: %d\n", len);
        if ((len < 1) || (line[len - 1] != '\n')) {
            fprintf(stderr, "read error");
            return -1;
        }
        while (len > 0) { //check for spaces from the back
            --len;
            if (line[len] != ' ' && line[len] != '\t') {
                ++len;
                break;
            }
        }
        line[len] = 0;
        double val;
        for (cur = line; *cur != 0; cur = end) {
            val = strtod(cur, &end);
            if (cur == end) {
                fprintf(stderr, "invalid input");
                return -1;
            }
            fprintf(stdout, "%f\n", val);
        }
    } 
    fclose(in_file);
    fclose(out_file);
    return 0;
}