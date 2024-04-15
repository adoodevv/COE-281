#include <stdio.h>

float calcArea(float rad);

int main()
{
   float radius, area;
   radius = 5.25;
   area = calcArea(radius);

   printf("The area of the circle with radius %g is %g\n", radius, area);
   return 0;
}

float calcArea(float rad)
{
   float a;
   a = 3.142 * rad * rad;
   return a;
}