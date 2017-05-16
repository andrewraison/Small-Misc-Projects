//Program to add yep integers typed by the user at keyboard
#include <iostream>
using namespace std;

int main()
{
	int a, b, total;

	cout << "Enter integers to be added:" << endl;
	cin >> a >> b;
	total = a + b;
	cout << "The sum is " << total << endl;

	return 0;
}