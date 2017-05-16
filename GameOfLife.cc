/* Conway’s Game of Life:
user inputs the number of generations to generate, and enters 0 to quit
the code must be edited to change starting position, 2 are in the main function (indicated)
there is a 10x10 board for the game to play out*/

#include <iostream>
using namespace std;

bool world[10][11];
bool getCell(int row, int col);
void setCell(int row, int col, bool value);
int countNeighbours(int row, int col);
bool computeCell(int row, int col);
void nextGeneration();
void print();

int main(){

	//starting positions follow, comment out the ones you don’t want or add more
		//simple glider
		world[0][1]=1;
		world[1][2]=1;
		world[2][0]=1;
		world[2][1]=1;
		world[2][2]=1;

		//the R-pentomino
		/*world[4][5]=1;
		world[4][4]=1;
		world[5][4]=1;
		world[5][3]=1;
		world[6][4]=1;*/


	print();
	int gennumb=1;
	while(gennumb!=0){
		cout << "Enter the number of generations you wish to generate, entering 0 will exit the program" << endl;
		cin >> gennumb;
		int count = gennumb;
		while (count>0){
			nextGeneration();
			print();
			clock_t start=clock();	//a time delay found on a forum to allow the user to watch the game
			while(clock() - start < 500000);
			count--;
		}
	}	
}

bool getCell(int row, int col){
	if ((col>10) || (col<0)) {return false;};
	if ((row>10) || (row<0)) {return false;};
	return world[row][col];
}

void setCell(int row, int col, bool value){
	if ((col>10) || (col<0)) {return;};
	if ((row>10) || (row<0)) {return;};
	world[row][col] = value;
}

int countNeighbours(int row, int col){
	int tmp = 0;
	for(int i=-1; i<2; i++){
		for(int j=-1; j<2; j++){
			tmp = tmp + getCell(row+i,col+j);
		}
	}
	tmp = tmp - getCell(row,col);
	return tmp;
}

bool computeCell(int row, int col){
	bool current = getCell(row,col);
	int neighbours = countNeighbours(row,col);
	bool next = false;
	switch(neighbours){
		case 3:
			next = true;
			break;
		case 2:
			if (current){next = true;}
			break;
		default: break;
	}
	return next;
}

void nextGeneration(){
			cout << endl;
	bool tmpworld[11][11];
	for(int row=0; row<10; row++){
		for(int col=0; col<10; col++){
			tmpworld[row][col] = computeCell(row,col);
		}
	}
	for(int row=0; row<10; row++){
		for(int col=0; col<10; col++){
			world[row][col]=tmpworld[row][col];
		}
	}
}

void print(){
	for(int row=0; row<10; row++){
		for(int col=0; col<10; col++){
			if(world[row][col]){cout << "#";}
				else{cout << "_";}
		}
		cout << endl;
	}
}