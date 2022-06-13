#include<iostream>

using namespace std;

int main() {
  int usin, usinEnd = '-';
  cout << "Enter Text: ";

  while ((usin = getchar()) != EOF) {
    if (usin == ' ') {
      if (usinEnd != ' ')
        putchar(usin);
    }
    else
      putchar(usin);
    usinEnd = usin;
  }
  return 0;
}