/* Dhruv Sakthivel 12/26/18

Program that prints the sum of 2 given numbers*/

#include <stdio.h>

int main()
{
	printf("Give me 2 numbers. Seperate them with a space: ");
	int val_2;
	int val_1;
	scanf("%d %d", &val_1, &val_2);
	int sum = val_1 + val_2;
	printf("%d\n", sum);
	return 0;

}