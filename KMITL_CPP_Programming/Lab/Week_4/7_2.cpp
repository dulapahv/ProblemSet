#include <iostream>

#define BUFFER_SIZE 81

int get_line(FILE *fp, char *buffer, int size) {
    char *end = buffer + size, *dst = buffer;
    int c;
    while ((c = fgetc(fp)) != EOF && c != '\n' && dst <= end) { // 
        *dst = c;
        dst++;
    }
    *dst = '\0';
    return ((c == EOF && dst == buffer) ? EOF : dst - buffer);
}

int main() {
    FILE *in_file = fopen("7_2in.txt", "rb");
    FILE *out_file = fopen("7_2out.txt", "wb");
    char *cur, *end, buffer[BUFFER_SIZE];
    for (int len; !feof(in_file);) {
        len = get_line(in_file, buffer, BUFFER_SIZE);
        if (len == -1)
            break;
        if ((len < 1) || (buffer[len - 1] != '\r')) {
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

        double val, partDiff, prev;
        for (cur = buffer; *cur != 0; cur = end) {
            val = strtod(cur, &end);
            if (cur == end) {
                fprintf(stderr, "invalid");
                return -1;
            }
            partDiff = val - prev;
            fprintf(out_file, "%.6g ", partDiff);
            prev = val;
        }
    }
}