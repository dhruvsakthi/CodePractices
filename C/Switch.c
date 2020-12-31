#include <stdio.h>
int main()
{
	int a;
	printf("Give me a value: ");
	scanf("%d", &a);
	int reverse_val = 0;
	while(a != 0)
	{
		reverse_val = 10 * reverse_val;
		reverse_val = reverse_val + a % 10;
		a = a / 10;
	}
	printf("the value is %d\n", reverse_val);
}	