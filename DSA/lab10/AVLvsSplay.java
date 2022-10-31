import java.util.Random;

// class AVLTree { // replace this class with the actual AVL class
//    void add(int n) {}
//    boolean search(int n) { return true; }
// }

// class SplayTree { // replace this class with the actual splay tree class
//     void add(int n) {
//     }

//     boolean search(int n) {
//         return true;
//     }
// }

public class AVLvsSplay {

    static int nextGaussian(Random r, int mean) {
        return (int) (r.nextGaussian() * mean / 2) + mean;
    }

    public static void main(String[] args) {
        int step = 1_000_000; // change to fit your machine
        int start = 1_000_000; // change to fit your machine

        Random r = new Random();

        SplayTree splay = new SplayTree();

        // AVL Tree, ordered build
        for (int n = start; n < start + 10 * step; n += step) {
            AVLTree avl = new AVLTree();
            System.out.println("n: " + n);
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.add(new Node(i), i);
            System.out.println("avl ordered build: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.search(new Node(i), i);
            System.out.println("avl ordered access: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.search(new Node(i), nextGaussian(r, n));
            System.out.println("avl gaussian access: " + (System.currentTimeMillis() - startTime));
            System.out.println();
        }

        // AVL Tree, random build
        for (int n = start; n < start + 10 * step; n += step) {
            AVLTree avl = new AVLTree();
            System.out.println("n: " + n);
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.add(new Node(i), r.nextInt(n));
            System.out.println("avl random build: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.search(new Node(i), i);
            System.out.println("avl ordered access: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                avl.search(new Node(i), nextGaussian(r, n));
            System.out.println("avl gaussian access: " + (System.currentTimeMillis() - startTime));
            System.out.println();
        }

        // Splay Tree, ordered build
        for (int n = start; n < start + 10 * step; n += step) {
            System.out.println("n: " + n);
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.add(new Node(i), i);
            System.out.println("splay ordered build: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.search(new Node(i), i);
            System.out.println("splay ordered access: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.search(new Node(i), nextGaussian(r, n));
            System.out.println("splay gaussian access: " + (System.currentTimeMillis() - startTime));
            System.out.println();
        }

        // Splay Tree, random build
        for (int n = start; n < start + 10 * step; n += step) {
            System.out.println("n: " + n);
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.add(new Node(i), r.nextInt(n));
            System.out.println("splay random build: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.search(new Node(i), i);
            System.out.println("splay ordered access: " + (System.currentTimeMillis() - startTime));

            startTime = System.currentTimeMillis();
            for (int i = 0; i < n; i++)
                splay.search(new Node(i), nextGaussian(r, n));
            System.out.println("splay gaussian access: " + (System.currentTimeMillis() - startTime));
            System.out.println();
        }
    }
}