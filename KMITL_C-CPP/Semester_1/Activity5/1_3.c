#include <stdio.h>

int main(int argc, char** argv) {
    for (int i = argc - 1; i >= 0; i--)
        printf("argv[%d] = [%s]\n", i, argv[i]);
    return 0;
}