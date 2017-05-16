/*Prints out a list of primes, up to a user specified number
User also decides whether to print out all primes or just the twin prime pairs*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	int p = 0, maxnumb, i=1, j=3, n,d;
	char answer;
	string input;

	//user decides whether the output will be all primes or just twin primes
	cout << "Do you only want to print out twin primes? (answer y/n)" << endl;
	while (p != 1){
		cin >> answer;
		if (answer != 'y' & answer != 'n'){
			cout << "You must answer with either y or n" << endl;
		} else {p = 1;}
	}
	

	//user decides how many primes to compute
	p=0;
	cout << "Enter the number of primes you wish to consider (positive integer)" << endl;
	while (p != 1){		
		cin >> input;
		stringstream stream(input);
		if (stream >> maxnumb){
			if (maxnumb > 0){
				break;}
		}
		cout << "You must enter a positive integer" << endl;
	}


	//loop where primes are calculated up to the number defined previously
	cout << endl;
	int primes[maxnumb];
	primes[0] = 2;
	while(i<maxnumb){
		bool m = false;
		for(n=0;n<i;n++){
			if ((j%(primes[n]))==0){
				m=true;
			}
		}
		if (!m) {
			primes[i]=j;
			i++;
		}
		j++;
	}


	//outputs the answer requested by the user
	if (answer == 'y'){
		for(int q=0; q<(maxnumb-1); q++){
			if ((primes[q+1]-primes[q])==2){
				cout << primes[q] << "\t" << primes[q+1] << endl;
			}
		}
	} else{
		for(int l=0;l<maxnumb;l++){
			cout << primes[l] <<endl;
		}
	}
}
