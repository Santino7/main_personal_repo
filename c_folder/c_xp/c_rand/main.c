//By Santino J. Tomasi
//Basic game movement left to right.
//Errors will occur if you move to far left or right!


#include <ncurses.h>
#include <string.h>


int find_i(char arr[],char ch);


int main(void)
{	
	
	initscr();
	noecho();

	char arr[] = {'.','x','.'};

	int power = 1;
	
	printw("%s",arr);

	while(power == 1){

		int i = find_i(arr,'x');

		char ch = getch();

		if(ch == 'a'){

			arr[i] = '.';
			arr[i-1] = 'x';
			
		}

		if(ch == 'd'){
			
			arr[i] = '.';
			arr[i+1] = 'x';
		}
		
		clear();
		printw("%s",arr);
		printw("%d",i);

		if(ch == 'q'){
			endwin();
			power = 0;
		}

	}
	
	return 0;
}


int find_i(char arr[],char ch){
	
	int i = 0;
	
	size_t x = sizeof(arr)/sizeof(arr[0]);

	while(i<x){
		
		if(arr[i] == ch){

			return i;
		}
	        
		i++;	
	}
}
