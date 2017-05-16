/*RootFind.cc
This will find the mth of n using the bisection method*/

#include <iostream>

using namespace std;

double rootFinder(int n,int m);
double sqrt(int n, double x,int m);


int main(){
	int n,m;
	cout << "insert the number you wish to find the root of" << endl;
	cin >> n;
	cout << "insert the root power you wish to find" << endl;
	cin >> m;

	cout << "The " << m << "th root of " << n << " is " << rootFinder(n,m) << endl;
}

//returns value of polynomial y = x^m - n;
double sqrt(int n, double x,int m){
	double acc=1;
	for(int i=0;i<m;i++){
		acc=acc*x;
	}
	return (acc - n);
	}

//uses bisection method to find the root
double rootFinder(int n,int m){
	if (n==0){return 0.0;}
	double a=0;
	double b=n;	//assert the root is between 0 and n, true for finding the nth root
	double ares,bres;
	ares = sqrt(n,a,m);
	bres = sqrt(n,b,m);
	
	for(int i=1;i<(n);i++){
		double tmp;
		tmp = sqrt(n,((a+b)/2),m);
		if(tmp==0){break;}
		if(((tmp>0) & (ares>0))||((tmp<0) & (ares<0))){
			a=(a+b)/2;
			ares=tmp;
		} else{
			b=(a+b)/2;
			bres=tmp;
		}
	}
	return (a+b)/2;
}
