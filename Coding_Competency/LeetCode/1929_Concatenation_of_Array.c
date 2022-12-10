#include <stdio.h>
#include <stdlib.h>

int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize * 2;
    int* returnArray = malloc(sizeof(int) * (numsSize * 2));
    int i = 0;
    int j = 0;
    while (i < numsSize * 2) {
        returnArray[i] = nums[j];
        i++;
        if (j == numsSize - 1) {
            j = 0;
        } else {
            j++;
        }
    }
    return returnArray;
}

int main() {
    int nums[3] = {1, 2, 1};
    int* returnSize;
    returnSize = getConcatenation(nums, 3, returnSize);
    for (int i = 0; i < 6; i++) {
        printf("%d ", returnSize[i]);
    }
}