#include <stdio.h>
#include <stdlib.h>

char* defangIPaddr(char* address) {
    char* ip;
    int i = 0;
    int padding = 0;
    int adjust = 0;
    ip = malloc(sizeof(char) * 22);
    while (address[i]) {
        if (address[i] == '.') {
            ip[i] = '[';
            ip[i + 1] = '.';
            ip[i + 2] = ']';
            padding += 3;
            adjust++;
        }
        ip[i + padding] = address[i + adjust];
        i++;
    }
    ip[i] == '\0';
    return ip;
}

int main() {
    char* ip = "111.111.111.111";
    printf("%s", defangIPaddr(ip));
}