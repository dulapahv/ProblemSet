    public class QuadraticProbing {
        public static void main(String[] args) {
            // create a list of numbers
            int[] random_list = { 17, 65, 91, 45, 18, 74, 62, 84, 32 };

            // create a hash table of size 11
            int[] hash_table = new int[11];

            // hash each number in the list and insert it into the hash table
            for (int i = 0; i < random_list.length; i++) {
                int pos = random_list[i] % 11;
                int c1 = 1;
                int c2 = 1;
                while (true) {
                    if (hash_table[pos] == 0) {
                        hash_table[pos] = random_list[i];
                        break;
                    } else {
                        pos = (pos + c1 * c2) % 11;
                        c2 += 1;
                    }
                }
            }

            // print the hash table
            for (int i : hash_table) {
                System.out.print(i + " ");
            }
        }
    }
