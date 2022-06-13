#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "@ime";
    char str2[] = "ToGo";
    char str3[] = "3ome";
    char all_strs[255];

    strcat(strcat(strcat(strcat(strcat(all_strs, str1), ","), str2), ","), str3);
    printf("%s", all_strs);
}