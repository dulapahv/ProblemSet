/**
 * ENGG1110 Problem Solving by Programming
 *
 * Course Project
 *
 * I declare that the project here submitted is original
 * except for source material explicitly acknowledged,
 * and that the same or closely related material has not been
 * previously submitted for another course.
 * I also acknowledge that I am aware of University policy and
 * regulations on honesty in academic work, and of the disciplinary
 * guidelines and procedures applicable to breaches of such
 * policy and regulations, as contained in the website.
 *
 * University Guideline on Academic Honesty:
 *   https://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Student Name  : Tnaban PONCHALEE
 * Student ID    : 1155168418
 * Class/Section : C
 * Date          : 15/11/2022
 */

#include <stdio.h>
/* NO other header files are allowed */
/* NO global variables are allowed */
/* Display the game board and the unused numbers list on the screen.
   You are required to exactly follow the output format stated in the project specification.
   IMPORTANT: Using other output formats will result in mark deduction. */

void printInfo(int gameBoard[3][3], int numbers[9]) {

    // TODO: Complete this part

    for (int i = 0; i < 3; i++) {
        printf("|");
            for (int j = 0; j < 3; j++) {
                if (gameBoard[i][j] == 0)
                     printf(" ");
                else printf("%d", gameBoard[i][j]);
                            printf("|");
            }
            printf("\n");
        }

    printf("Unused numbers:\n");
            for (int k = 0; k < 9; k++) {
                if (numbers[k] == 0)
                    printf("%d ", k+1);
            }
}

/* Read the user inputs to place a number on the game board.
   In Project Part 1, you can assume that the user inputs must be valid. */

void placeNumber(int gameBoard[3][3], int numbers[9], int currentPlayer) {

    // TODO: Complete this part

 int position, number, k = 1;

    printf("\n### Player %d's turn ###", currentPlayer);
        printf("\nInput the position: ");
            scanf("%d", &position);

        printf("Input the number: ");
            scanf("%d", &number);

    for (int i = 2; i >= 0; i--) {
            for (int j = 0; j < 3; j++) {
                    if (k == position) {
                        gameBoard[i][j] = number;
                        numbers[number-1] = 1;
                    }
                        k++ ;
            }
    }
}

/* Return 1 if there is a winner in the game, otherwise return 0.
   Note: the winner is the current player indicated in main(). */

int hasWinner(int gameBoard[3][3]){

    // TODO: Complete this part

    for (int i = 0; i < 3; i++){
            if ((gameBoard[i][0] + gameBoard[i][1] + gameBoard[i][2] == 15)
                && (gameBoard[i][0] != 0) && (gameBoard[i][1] != 0) && (gameBoard[i][2] != 0))
                return 1;

            if ((gameBoard[0][i] + gameBoard[1][i] + gameBoard[2][i] == 15)
                && (gameBoard[0][i] != 0) && (gameBoard[1][i] != 0) && (gameBoard[2][i] != 0))
                return 1;
    }

    if ((gameBoard[0][0] + gameBoard[1][1] + gameBoard[2][2] == 15)
        && (gameBoard[0][0] != 0) && (gameBoard[1][1] != 0) && (gameBoard[2][2] != 0))
                return 1;

    if ((gameBoard[2][0] + gameBoard[1][1] + gameBoard[0][2] == 15)
        && (gameBoard[2][0] != 0) && (gameBoard[1][1] != 0) && (gameBoard[0][2] != 0))
                return 1;

 return 0;
}



/* Return 1 if the game board is full, otherwise return 0. */
int isFull(int gameBoard[3][3]) {

    // TODO: Complete this part
 int fulfill = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (gameBoard[i][j] != 0)
                fulfill++;
        }
    }
    if (fulfill == 9)
        return 1;
    else return 0;
}

/* The main function */

int main() {

    /* Local variables, you can declare more if necessary */

    int gameBoard[3][3] = {0};      /* A 2D array presenting the game board.
                                       Each element stores a number between 0 and 9 inclusively, where 0 represents an empty cell. */
    int numbers[9] = {0};           /* An array to record which numbers are used by the players.
                                       Example: if numbers[0] is 1, the number 1 is used
                                                if numbers[1] is 0, the number 2 is not used
                                                if numbers[8] is 1, the number 9 is used */
    int currentPlayer;              // 1: Player 1             2: Player 2
    int gameContinue;               // 1: The game continues   0: The game ends

    /* Initialize the local variables */
    currentPlayer = 1;
    gameContinue = 1;

    /* Uncomment the following statements to test whether the printInfo(...)
       and the placeNumber(...) functions are implemented correctly.
       You can add more if you wish.
       After testing, you can delete them. */

        /* Game start, Player 1 moves first */

    // TODO: Complete this part

    printInfo(gameBoard, numbers);

        while (gameContinue == 1) {
            placeNumber(gameBoard, numbers, currentPlayer);
            printInfo(gameBoard, numbers);
                if (hasWinner(gameBoard) == 1) {
                break;
                }
                    if (isFull(gameBoard) == 1) {
                    gameContinue = 0;
                    break;
                    }
            currentPlayer++;

            placeNumber(gameBoard, numbers, currentPlayer);
            printInfo(gameBoard, numbers);
                if (hasWinner(gameBoard) == 1) {
                break;
                }
            currentPlayer--;
        }

    if (gameContinue == 0)
         printf("\nDraw game.");
    else printf("\nCongratulations! Player %d wins!", currentPlayer);

 return 0;

}
