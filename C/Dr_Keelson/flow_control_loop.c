#include <stdio.h>

int main()
{
   // while loop
   int q = 5;

   while(q < 10)
   {
      printf("%d\n", q);
      q++; // increment q by 1
   }

   // do while loop
   int m = 12;

   do
   {
      printf("%d\t", m);
      m++;
   } while (m < 20);
   
   // for loop
   int a;
   for (a = 0; a < 4; a++)
   {
      printf("%d\n", a);
   }
   
   return 0;
}