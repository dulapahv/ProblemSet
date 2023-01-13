import java.util.Arrays;

class ActivitySelection {
    public static int printMaxActivities(int start[], int end[], int n) {
        if (n == 1) {
            return 1;
        }

        int arr[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = start[i];
            arr[i][1] = end[i];
        }

        Arrays.sort(arr, (b, c) -> Double.compare(b[1], c[1]));

        int j = -1;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i][0] > j) {
                count++;
                j = arr[i][1];
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int start[] = { 53, 3, 51, 67, 37, 3, 24, 28, 1, 24, 3, 4, 18, 45, 44, 32, 28, 29, 33, 83, 30, 4, 29, 41, 74,
                31, 88, 81, 30, 48, 40, 1, 69, 28, 49, 28, 45, 12, 25, 28, 90, 50, 23, 11, 3, 6, 14, 29, 51, 38, 13, 15,
                24, 33, 6, 17, 18, 35 };
        int end[] = { 97, 6, 100, 95, 92, 80, 30, 72, 84, 47, 54, 95, 52, 70, 45, 56, 34, 40, 87, 87, 35, 53, 44, 45,
                87, 32, 91, 86, 36, 76, 59, 87, 87, 45, 66, 91, 70, 93, 50, 46, 93, 89, 62, 71, 76, 66, 31, 86, 62, 100,
                19, 40, 56, 66, 15, 78, 22, 58 };
        int n = start.length;

        System.out.println(printMaxActivities(start, end, n));
    }
}
