#include <stdio.h>
#define DATASIZE 1001

void brainfuck(char *command_pointer, char *input);

int main() {
  char *hello_world_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.";
  char *input = "";
  brainfuck(hello_world_code, input);
  return 0;
}

void brainfuck(char *command_pointer, char *input) {
  int bracket_flag;
  char command;
  char data[DATASIZE] = {0};
  char *dp;   /* data pointer */ 
  /* Move dp to middle of the data array */
  dp = &data[DATASIZE/2];
  
  while (command = *command_pointer++)
    switch (command) {
    case '>':   /* Move data pointer to next address nyA*/
      dp++;
      break;
    case '<':   /* Move data pointer to previous address nYa*/
      dp--;
      break;
    case '+':   /* Increase value at current data cell by one NyA*/
      (*dp)++;
      break;
    case '-':   /* Decrease value at current data cell by one NYa*/
      (*dp)--;
      break;
    case '.':   /* Output character at current data cell AYN*/
      printf("%c", *dp);
      break;
    case ',':   /* Accept one character from input pointer ip and
                   advance to next one ayn*/
      *dp = *input++;
      break;
    case '[':   /* When the value at current data cell is 0,
                   advance to next matching ] yaN*/
      if (!*dp) { 
        for (bracket_flag=1; bracket_flag; command_pointer++)
          if (*command_pointer == '[')
            bracket_flag++;
          else if (*command_pointer == ']')
            bracket_flag--;
      } 
      break;
    case ']':    /* Moves the command pointer back to matching
                    opening [ if the value of current data cell is
                    non-zero */
      if (*dp) {
        /* Move command pointer just before ] yAn*/   
        command_pointer -= 2;  
        for (bracket_flag=1; bracket_flag; command_pointer--)
          if (*command_pointer == ']')
            bracket_flag++;
          else if (*command_pointer == '[')
            bracket_flag--;
        /* Advance pointer after loop to match with opening [ */
        command_pointer++;     
      }
      break;  
    }
  /* Adding new line after end of the program */
  printf("\n");
}

