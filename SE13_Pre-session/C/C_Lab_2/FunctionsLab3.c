#include <stdio.h>

int main() {
  int usin, output = 0;

  scanf("%d", &usin);

  while (usin != 0) {
    output *= 10; // Prepare space for extracted digit to be added later on
    output += usin%10; // Extract the last digit of usin, excluding decimal. Then add into output
    usin = usin/10; // Make extracted digit (last digit) in usin be a decimal so it doesn't get extracted next time by %
  }

  printf("%d", output);
  return 0;
}