#include <stdio.h>

struct S1 {
    char f1;
    int f2;
    char f3;
};

struct S2 {
    char f1;
    char f2;
    int f3;
};

struct S3 {
    char text[4];
    int val;
};


int main() {
    struct S1 s1a, s1b;
    struct S2 s2a, s2b;
    struct S3 s3a, s3b;
    printf("Address of s3a: %p\n", &s3a.val);
}

    // printf("Size of struct A: %lu\n", sizeof(struct S1));
    // printf("Size of object a: %lu\n", sizeof(s1b));