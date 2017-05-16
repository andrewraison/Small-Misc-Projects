/*PiII.cc
Method for estimating pi using the sum of 1/i^2 to infinity, which converges at pi^2/6

Useage: ./PiII [(N)]
	(if nothing is entered, N defaults to 100)
	After the iteration has finished, you get the option to continue the iteration for a user determined number of iterations

To be accurate to 2 dp: rounds to 3.14 after about 150 iterations, and is comfortably to 2 dp after 300 iterations (~3.138)*/

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char* argv[]){
	int N=100,n=1,a=1,b;
	double answer=0,estimate;

	if (argc>1){
		sscanf(argv[1], "%d", &N);
	}

	while(a<=N){
		answer = answer + 1.0/(1.0*n*n);
		estimate = sqrt(answer*6.0);
		cout << "Current estimate " << estimate << endl;
		if(a==(N-1)){
			cout <<  "How more iterations do you want to do? (positive integer value)" << endl;
			cin >> b;
			a=a-b;
		}
		n++;
		a++;
	}
}
