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