//I do not know.
//By Santino J. Tomasi


#include <stdio.h>
#include <stdlib.h>


int main(void)
{
	char *str;

	int inc = 0;

	while ( 1 )
	{
		char ch = getc(stdin);

		printf("hi1");

		if ( ch == 0 || ch == '\n' )
		{
			str[inc] = (char)ch;

			printf("%s", str);

			exit(0);
		}


		str[inc] = (char)ch;

		size_t str_z = sizeof(str) / sizeof(char);

		str = realloc(str,  4 * sizeof(char));

		inc++;

	}
	

	return 0;
}
