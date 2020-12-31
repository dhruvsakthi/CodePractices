/* Dhruv Sakthivel 12/26/18

Program that gets 3 values (principle, rate, and time) and calculates the simple interest 8*/

#include <stdio.h>

int main()
{
	float P;
	int R;
	int T;
	printf("This is the simple interest calculator.........................................\n");
	printf("...............................................................................\n");
	printf("Enter the principle, rate(in percent), and time(in years), seperated by a space: ");
	scanf("%f %d %d", &P, &R, &T);
	float rate = R * 0.01;
	float interest = (P * rate * T);
	printf("The interest is $%02f \n", interest);
	printf("The final amount is: $%02f\n", interest + P);
	return 0;

}