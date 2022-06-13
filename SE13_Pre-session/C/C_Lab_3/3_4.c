#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[255];

    fp = fopen("sample.txt", "r");
    while (fgets(buffer, 255, (FILE*)fp) != NULL) {
        printf("%s\n", buffer);
    }
    fclose(fp);
}