#include <iostream>
int main()
{
FILE *inFile = fopen("counting.txt", "r");

using namespace std;

char c;
int d =0;
int n=0;
int t=0;
int total=0;
    cout << "Enter the statement to count blanks tabs lines: \n" << endl;

while((c = fgetc(inFile)) != EOF)
{
    if(c == ' ')
    {
        ++d;
        ++total;
    }
    else if(c == '\t')
    {
        ++t;
        ++total;
    }
    else if(c == '\n')
    {
        +n;
        ++total;
    }
}
    cout << "the number of count blanks: " << d << endl;
    cout << "the number of count tabs: " << t << endl;
    cout << "the number of count lines: " << n << endl;
    cout << "the number of total count: " << total << endl;
}