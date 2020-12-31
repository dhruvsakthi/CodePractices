/* Dhruv Sakthvel 12/26/18

Program that swaps 2 numbers' value using 2 variables*/

#include <stdio.h>

int main()
{
	int a;
	int b;
	printf("give me 2 whole numbers to swap values: ");
	scanf("%d %d", &a, &b);
	a = a + b;
	b = a - b;
	a = a - b;
	printf("a = %d\n", a);
	printf("b = %d\n", b);
}