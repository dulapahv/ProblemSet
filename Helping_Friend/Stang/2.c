#include <stdio.h>

/* starting point of this C program */

int main(void)
{
	int phoneNum;
	int digit;
	int uniqueNum = 0;
	int digitCount[10] = {0};

	scanf("%d", &phoneNum);

	if (phoneNum < 10000000 || phoneNum > 99999999) {
		printf("Invalid phone number.");
		return 0;
	}

	for (int i = 0; i < 8; i++) {
		digit = phoneNum % 10;
		phoneNum /= 10;
		digitCount[digit]++;

		if (i == 7 && (digit == 0 || digit == 1)) {
			printf("Invalid phone number.");
			return 0;
		}
	}

	for (int i = 0; i < 10; i++) {
		if (digitCount[i] >= 1)
			uniqueNum++;
	}

	printf("There are %d unique digit(s).", uniqueNum);
}