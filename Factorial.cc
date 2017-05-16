/*Basic factorial function and some thermo work*/
#include <iostream>

using namespace std;

int factorial(int x);
double g(int N, int m);

int main(int argc, char* arg[]){
	int a;

	sscanf(arg[1],"%d",&a);

	cout << factorial(a) << endl;
}


int factorial(int x){
	if (x>1){
		return x*factorial(x-1);
	}
	else { if (x==1 || x==0){
		return 1;
		}
		else {return -1;}
	}
}
