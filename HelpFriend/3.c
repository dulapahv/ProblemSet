#include <stdio.h>

struct S {
    int val;
    char text[4];
};

union Ex1 {
    char b;
    char c;
    int x;
    int y;
    char text[4];
    struct S s_val;
};


int main() {
    union Ex1 x1;
    x1.x = 0xDEADBEEF;
    printf("%p", &x1.s_val.text);
}
