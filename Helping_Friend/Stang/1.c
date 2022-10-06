#include <stdio.h>

#define N 10

int main() {
	/* 1 */
	int votes[N] = {0};
	
	/* 2a and 2c */
	for (int i = 0; i < N; i++) {
		scanf("%d", &votes[i]);
		
		/* 2b */
		if (votes[i] < 0 && votes[i] > 3) {
			printf("We cannot decide our committee chairman in this vote.");
			return 0;
		}
	}

	/* 3 */
	int count1 = 0, count2 = 0, count3 = 0;
	for (int i = 0; i < N; i++) {
		if (votes[i] == 1)
			count1++;
		else if (votes[i] == 2)
			count2++;
		else if (votes[i] == 3)
			count3++;
	}

	/* 4 5 */
	int candidateNum;
	if (count1 > count2 && count1 > count3)
		candidateNum = 1;
	else if (count2 > count1 && count2 > count3)
		candidateNum = 2;
	else if (count3 > count1 && count3 > count2)
		candidateNum = 3;
	else {
		printf("We cannot decide our committee chairman in this vote.");
		return 0;
	}

	/* 6 */
	printf("Congratulations! Candidate %d is the next committee chairman.", candidateNum);
}