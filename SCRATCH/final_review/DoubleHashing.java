public class DoubleHashing {

    public static void main(String[] args) {
        // create a list of numbers
        int random_list[] = { 17, 65, 91, 45, 18, 74, 62, 84, 32 };

        // create a hash table
        int hash_table[] = new int[11];

        // hash each number in the list and insert it into the hash table where h(x) =
        // H(x) + iG(x)
        for (int i : random_list) {
            int pos = i % 11;
            int c = 1;
            while (true) {
                if (hash_table[pos] == 0) {
                    hash_table[pos] = i;
                    break;
                } else {
                    pos = i % 11; // Reset pos to initial position
                    pos = (pos + c * (pos + hash_table[pos])) % 11;
                    c += 1;
                }
            }
        }

        // print the hash table
        for (int i : hash_table) {
            System.out.print(i + " ");
        }
    }
}