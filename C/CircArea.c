/*Dhruv Sakthivel 12/26/18

Program that gets the radius from the user, and prints out the circumference and the area. */

#include <stdio.h>

int main()
{
	int radius; 
	printf("Insert the radius value: ");
	scanf("%d", &radius);
	float Circ = (2 * radius * 3.141592);
	float Area = ((radius * radius) * 3.141592);
	printf("This is the cricumference: %f\n", Circ);
	printf("THis is the area: %f\n", Area);
	return 0;
}