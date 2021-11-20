#include <stdio.h>

int main(int argc, char** argv) {
    for (char** i = argv; i < argv + argc; i++)
        printf("argv[%d] = [%s]\n", i - argv, *i);
    return 0;
} 