#include <iostream>

using namespace std;

int main()
{
	//write program to generate FIBONACII series upto n terms using array
	static int arr[4000000], i, n;
	// cout<<"Enter Number of Fibonacci Terms required:";
	cin >> n;
	// Since first two terms are 0,1
	arr[0] = 0;
	arr[1] = 1;
	// use for loop to find remaining terms
	for (i = 2; i < n; i++)
		arr[i] = arr[i - 1] + arr[i - 2];

	// cout<<"Required "<<n<<" Fibonaccii Terms are:"<<endl;
	int result;
	for (i = 0; i < n; i++)
		if (arr[i] % 2 == 0)
		{
			result += arr[i];
		}
	// cout<<arr[i]<<", ";
	cout << result;
	return 0;
}