import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int count = 0;
        while (n != 1) {
            if (n % 3 == 0) {
                n /= 3;
            } else {
                n -= 1;
            }
            count++;
        } 
        System.out.println(count);
        scanner.close();
    }
}