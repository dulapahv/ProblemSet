#include <iostream>

#define BUFFER_SIZE 81

using namespace std;

int get_line(FILE *fp, char *buffer, int size) {
    char *end = buffer + size;
    char *dst = buffer;
    int c;
    while ((c = fgetc(fp)) != EOF && c != '\n' && dst <= end) {
        *dst = c;
        dst++;
    }
    *dst = '\0';
    return ((c == EOF && dst == buffer) ? EOF : dst - buffer);
}

int main() {
    FILE *in_file = fopen("6in.txt", "rb");
    char *cur, *end, buffer[BUFFER_SIZE];
    double n, sum, sum2, sum3, min = 9999999999, max = 0;
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

        double val;
        for (cur = buffer; *cur != 0; cur = end) {
            val = strtod(cur, &end);
            if (cur == end) {
                fprintf(stderr, "invalid");
                return -1;
            }
            sum += val;
            sum2 += val * val;
            sum3 += val * val * val;
            if (val < min)
                min = val;
            if (val > max)
                max = val;
            n++;
        }
    }

    cout << "sum(x) = " << sum << endl;
    cout << "average(x) = " << sum / n << endl;
    cout << "min(x) = " << min << endl;
    cout << "max(x) = " << max << endl;
    cout << "sum(x**2) = " << sum2 << endl;
    cout << "sum(x**3) = " << sum3 << endl;

    fclose(in_file);
}