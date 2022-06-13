#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Character {
    char name[80];
    int maxHP;
    double atk;
} character;

void character_stat_up(character *character) {
    character->maxHP += 5;
    character->atk += 0.1;
    if (character->maxHP > 9999)
        character->maxHP = 9999;
    if (character->atk > 90000.0)
        character->atk = 90000.0;
}

int main() {

}