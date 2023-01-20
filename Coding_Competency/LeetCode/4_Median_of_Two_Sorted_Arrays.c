#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    double median = 0;
    int len = nums1Size + nums2Size;
    int* nums3 = calloc(len, sizeof(int));
    int i = 0, j = 0, k = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) {
            nums3[k] = nums1[i];
            i++;
        } else {
            nums3[k] = nums2[j];
            j++;
        }
        k++;
    }
    while (i < nums1Size) {
        nums3[k] = nums1[i];
        i++;
        k++;
    }
    while (j < nums2Size) {
        nums3[k] = nums2[j];
        j++;
        k++;
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