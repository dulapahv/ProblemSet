import java.io.*;
import java.util.*;

class CoinChange {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int sum = sc.nextInt();
            int N = sc.nextInt();
            int coins[] = new int[N];
            for (int i = 0; i < N; i++)
                coins[i] = sc.nextInt();
            Solution ob = new Solution();
            System.out.println(ob.count(coins, N, sum));
        }
    }
}

class Solution {
    public long count(int coins[], int N, int sum) {
        long dp[][] = new long[N + 1][sum + 1];

        // Base Cases
        for (int i = 0; i <= N; i++)
            dp[i][0] = 1;

        // Fill the dp[ ][ ] table in bottom-up manner
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= sum; j++) {
                if (j >= coins[i - 1])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]];
                else
                    dp[i][j] = dp[i - 1][j];
            }

        return dp[N][sum];
    }
}