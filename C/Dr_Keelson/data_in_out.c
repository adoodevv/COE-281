#include <stdio.h>

int main()
{
   // printing output with printf
   int age = 28;
   float weight = 60.54;
   printf("I am %d years old and I weigh %g kilograms\n", age, weight);
   
   // taking input from user with scanf
   int personAge;
   scanf("%d", &personAge);

   // multiple user input
   float score_1, score_2, score_3;
   scanf("%g %g %g", &score_1, &score_2, &score_3);
   
   // getchar and putchar
   char choice = getchar();
   putchar(choice);

   return 0;
}