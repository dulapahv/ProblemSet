#include <stdio.h>

int main(int argc, char** argv) {
    for (char** i = argv + argc - 1; i >= argv; i--)
        printf("argv[%d] = [%s]\n", i - argv, *i);
    return 0;
} 