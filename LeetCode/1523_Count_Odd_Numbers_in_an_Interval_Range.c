// class Solution(object):
//     def countOdds(self, low, high):
//         return len([num for num in range(low, high + 1) if num & 1 == 1])

// print(Solution().countOdds(3, 7))

#include <stdio.h>

int countOdds(int low, int high) {
    int ans = (high - low) / 2;
    if (low & 1 || high & 1)
        ans++;
    return ans;
}

int main()
{
    printf("%d", countOdds(8, 10));
}