#include <iostream>
#include <stdlib.h>
#include <stdio.h> 
#include <string.h>
using namespace std;
class Game {
public:
	int board [4][4]= {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
	int* adboard [2][4][4]= {{{&board[0][0],&board[0][1],&board[0][2],&board[0][3]},{&board[1][0],&board[1][1],&board[1][2],&board[1][3]},{&board[2][0],&board[2][1],&board[2][2],&board[2][3]},{&board[3][0],&board[3][1],&board[3][2],&board[3][3]}},{{&board[0][0],&board[1][0],&board[2][0],&board[3][0]},{&board[0][1],&board[1][1],&board[2][1],&board[3][1]},{&board[0][2],&board[1][2],&board[2][2],&board[3][2]},{&board[0][3],&board[1][3],&board[2][3],&board[3][3]}}};
	int statics [4][4]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
	int score = 0;
	void show ();
	void move(int direction);
	void addTile();
	int moveLine(int start, int direction, int column);
	int moveDir(int lis[], int column);
};
void Game::show(){
	printf(" %d %d %d %d \n %d %d %d %d \n %d %d %d %d \n %d %d %d %d \n",board[0][0],board[0][1],board[0][2],board[0][3],board[1][0],board[1][1],board[1][2],board[1][3],board[2][0],board[2][1],board[2][2],board[2][3],board[3][0],board[3][1],board[3][2],board[3][3]);
}
void Game::addTile(){
	int tile = (((rand() % 2)+1)*2); 
	int placeX = rand()%4;
	int placeY = rand()%4;
	while (board[placeY][placeX] != 0){
		placeX = rand()%4;
		placeY = rand()%4;
	}
	board[placeY][placeX] = tile;
}
int Game::moveLine(int start, int direction, int column) {
	int moved = 0;
	for (int i=0; i<4; i++){
		if (*adboard[column][start][i]!=0 && statics[start + direction][i]==0){
			if (statics[start][i]==0 && *adboard[column][start + direction][i] == *adboard[column][start][i]){
				*adboard[column][start+direction][i]=*adboard[column][start+direction][i]*2;
				statics[start+direction][i]=1;
				score+=*adboard[column][start+direction][i];
				*adboard[column][start][i]=0;
			} if (*adboard[column][start+direction][i]==0) {
				*adboard[column][start+direction][i]=*adboard[column][start][i];
				*adboard[column][start][i] = 0;
			}
			moved+=1;
		}
	}
	return moved;
}
int Game::moveDir(int lis[], int column) {
	int moved = 0;
	for (int i=0; i<6; i++){
		moved+=moveLine(lis[i],lis[0]*2-3,column);
	}
	return moved;

}
void Game::move(int direction){
	int moved = 0;
	memset(statics, 0, sizeof(statics));
	if (direction == 1){
		int lis[] = {1,2,3,1,2,1};
		moved = moveDir(lis, 0);
	} else if (direction == 2){
		int lis[] = {2,1,0,2,1,2};
		moved = moveDir(lis, 1);
	} else if (direction == 3){
		int lis[] = {2,1,0,2,1,2};
		moved = moveDir(lis, 0);
	} else if (direction == 4){
		int lis[] = {1,2,3,1,2,1};
		moved = moveDir(lis, 1);
	} if (moved>0){
		addTile();
	} else {
		cout << "can't move that way \n";
	}
	show();
}
int main () {
	Game game;
	game.addTile();
	game.addTile();
	game.show();
	for (int i=0; i<=10; i+=1) {
		int direction;
		cin >> direction;
		game.move(direction);
	}
	return 1;
}



