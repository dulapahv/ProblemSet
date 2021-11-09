#include <stdio.h>
#include <string.h>

int main() {
    char str1[10], str2[10];
    scanf("%s", str1);
    scanf("%s", str2);
    strcat(str1, ",");
    strcat(str1, str2);
    puts(str1);
  }