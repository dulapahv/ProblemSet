#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Character {
    char name[80];
    int maxHP;
    double atk;
} character;

void character_init(character *character) {
    strcpy(character->name, "Unknown");
    character->maxHP = 100;
    character->atk = 1.0;
}

void character_stat_up(character *character) {
    character->maxHP += 5;
    character->atk += 0.1;
    if (character->maxHP > 9999)
        character->maxHP = 9999;
    if (character->atk > 90000.0)
        character->atk = 90000.0;
}

character *character_create() {
    character *charPtr = malloc(sizeof(*charPtr));
    character_init(charPtr);
    return charPtr;
}

void character_delete(character *charPtr) {
    free(charPtr);
}

int main() {
    character *ptr;
    ptr = character_create();
    puts(ptr->name);
    printf("%d\n", ptr->maxHP);
    printf("%.1lf\n\n", ptr->atk);

    character_stat_up(ptr);
    puts(ptr->name);
    printf("%d\n", ptr->maxHP);
    printf("%.1lf\n\n", ptr->atk);

    character_stat_up(ptr);
    puts(ptr->name);
    printf("%d\n", ptr->maxHP);
    printf("%.1lf\n\n", ptr->atk);

    character_delete(ptr);
}