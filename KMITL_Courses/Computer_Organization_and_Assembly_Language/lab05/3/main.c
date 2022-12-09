#include <stdio.h>

int main() {
	FILE *fp = fopen("Makefile", "r");
	if (!fp) {
		printf("Makefile not found!\n");
		return 1;
	}
	char c;
	while ((c = fgetc(fp)) != EOF) {
		printf("%c", c);
	}

	printf("\n\n");
	fseek(fp, 0, SEEK_SET);

	while ((c = fgetc(fp)) != EOF) {
		printf("%x ", c);
	}
	fclose(fp);
	return 0;
}