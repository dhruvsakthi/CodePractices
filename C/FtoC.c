/* Dhruv Sakthivel 12/25/18

Program that prints out Farenheit to Celsius conversions, starting from 300, and ending at 0. 8 */

#include <stdio.h>


int main()
{
	// Defining loop that starts from 300, and makes it decreases.
	for (float Farenheit = 300; Farenheit >= 0; Farenheit--)
	{
		// using the Conversion Formula

		float Celsius = (((Farenheit - 32) * 5) / 9);

		//Printing the values

		printf("%f degrees farenheit is %.2f Celsius\n", Farenheit, Celsius);
	}
	return 0;
}