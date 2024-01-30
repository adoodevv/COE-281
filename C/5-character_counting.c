#include <stdio.h>

/* count characters in input */
int main () {
   long nc;
   nc = 0;
   while (getchar() != EOF)
      ++nc; /* increment by one */
   printf("%1d\n", nc);
}