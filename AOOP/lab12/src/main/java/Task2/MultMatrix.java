/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
class Worker implements Runnable {

    final int row;
    final int col;
    final int[][] A;
    final int[][] B;
    final int[][] C;

    public Worker(int row, int col, int[][] A, int[][] B, int[][] C) {
        this.row = row;
        this.col = col;
        this.A = A;
        this.B = B;
        this.C = C;
    }

    @Override
    public void run() {
        C[row][col] = (A[row][0] * B[0][col]) + (A[row][1] * B[1][col]);
    }
}

public class MultMatrix {

    static final int M = 3;
    static final int N = 3;

    static int[][] A = {{1, 0}, {3, -2}, {1, 4}};
    static int[][] B = {{1, 2, 3}, {4, 5, 6}};
    static int[][] C = new int[M][N];
    static Thread Threads[][] = new Thread[3][3];

    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                Threads[i][j] = new Thread(new Worker(i, j, A, B, C));
                Threads[i][j].start();
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                Threads[i][j].join();
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(C[i][j] + " ");
            }
            System.out.println();
        }
    }
}
