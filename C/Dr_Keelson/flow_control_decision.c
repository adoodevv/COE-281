#include <stdio.h>

int main()
{
   // decision statements - if else
   int x;
   printf("Please enter an integer value:\n");
   scanf("%d", &x);

   if(x % 2 == 0)
   {
      printf("%d is even\n", x);
   }
   else
   {
      printf("%d is odd\n", x);
   }

   // decision statements - switch
   int choice;
   printf("Are you a Ghanaian?\n");
   printf("Enter 1 for Yes and 2 for no:\n");
   scanf("%d", &choice);

   switch (choice)
   {
   case 1:
      printf("Ghanaians are hospitable people\n");
      break;
   case 2:
      printf("I don't know much about your country\n");
      break;   
   default:
      printf("You didn't follow the instruction\n");
      break;
   }
   return 0;
}