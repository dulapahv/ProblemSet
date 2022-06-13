#include <stdio.h>
#include <string.h>

struct Student {
    int id;
    char name[30];
    float sub1, sub2, sub3;
};

int main() {
    struct Student student[5];

    student[0].id = 21000001;
    strcpy(student[0].name, "Joe");
    student[0].sub1 = 72.5;
    student[0].sub2 = 85.2;
    student[0].sub3 = 59.4;

    student[1].id = 21000002;
    strcpy(student[1].name, "John");
    student[1].sub1 = 62.2;
    student[1].sub2 = 75.1;
    student[1].sub3 = 84.2;

    student[2].id = 21000003;
    strcpy(student[2].name, "Alice");
    student[2].sub1 = 82.4;
    student[2].sub2 = 65.4;
    student[2].sub3 = 91.1;

    student[3].id = 21000004;
    strcpy(student[3].name, "Bob");
    student[3].sub1 = 78.1;
    student[3].sub2 = 90.3;
    student[3].sub3 = 71.5;

    student[4].id = 21000005;
    strcpy(student[4].name, "Mary");
    student[4].sub1 = 90.3;
    student[4].sub2 = 82.5;
    student[4].sub3 = 61.3;

    float total[3] = {0};
    for (int i = 0; i < 5; i++) {
        total[0] += student[i].sub1 / 5;
        total[1] += student[i].sub2 / 5;
        total[2] += student[i].sub3 / 5;
    }
    for (int i = 0; i < 3; i++)
        printf("Sub%d average = %.1f\n", i, total[i]);
    return 0;
}