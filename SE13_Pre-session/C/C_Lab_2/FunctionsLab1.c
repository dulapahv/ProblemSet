#include <stdio.h>

#define size 20

int main() {
    char name[size], surname[size], nickname[size];
    int age;

    printf("Enter your first name: ");
    scanf("%s", name);
    printf("Enter your surname: ");
    scanf("%s", surname);
    printf("Enter your nickname: ");
    scanf("%s", nickname);
    printf("Enter your age: ");
    scanf("%d", &age);

    printf("My name is %s %s\nor you can call me \"%s\"\nI'm %d years old.", name, surname, nickname, age);
    return 0;
}