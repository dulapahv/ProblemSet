#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    double median = 0;
    int* nums3 = calloc((nums1Size + nums2Size), sizeof(int));
    int i = 0;
    int len = 0;
    while (i < nums1Size) {
        nums3[i] = nums1[i];
        i++;
        len++;
    }
    int j = 0;
    while (j < nums2Size) {
        nums3[i] = nums2[j];
        j++;
        i++;
        len++;
    }
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (nums3[i] > nums3[j]) {
                int temp = nums3[i];
                nums3[i] = nums3[j];
                nums3[j] = temp;
            }
        }
    }
    if (len % 2 != 0) {
        double ans = nums3[len / 2];
        free(nums3);
        return ans;
    } else {
        double ans = (nums3[(len / 2) - 1] + nums3[(len / 2)]) * 0.5;
        free(nums3);
        return ans;
    }
}

int main() {
    int nums1[2] = {4, 2};
    int nums2[2] = {3, 1};
    int nums1Size = 2;
    int nums2Size = 2;
    printf("%lf", findMedianSortedArrays(nums1, nums1Size, nums2, nums2Size));
}