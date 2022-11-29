public class LinearProbing {
    public static void main(String[] args) {
        // create a list of numbers
        int[] random_list = { 17, 65, 91, 45, 74, 62, 84, 32 };

        // create a hash table of size 11
        int[] hash_table = new int[11];

        // hash each number in the list and insert it into the hash table
        for (int i : random_list) {
            int pos = i % 11;
            while (true) {
                if (hash_table[pos] == 0) {
                    hash_table[pos] = i;
                    break;
                } else {
                    pos = (pos + 1) % 11;
                }
            }
        }

        // print the hash table
        for (int i : hash_table) {
            System.out.print(i + " ");
        }
    }
}
