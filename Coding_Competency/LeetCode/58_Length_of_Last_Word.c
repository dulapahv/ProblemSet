#include <stdio.h>

int lengthOfLastWord(char* s) {
    int end = 0;
    int flag = 0;
    while (s[end]) {
        if (s[end] == ' ' && flag == 0) {
            flag = 1;
        }
        end++;
    }
    if (flag == 0) {
        return end;
    }
    end--;
    while (end >= 0 && s[end] == ' ') {
        end--;
    }
    int start = end;
    while (start >= 0 && s[start] != ' ') {
        start--;
    }
    return end - start;
}

int main() {
    printf("%d", lengthOfLastWord("a"));
}