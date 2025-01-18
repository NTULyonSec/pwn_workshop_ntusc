#include <stdio.h>
#include <stdlib.h>

int win()
{
system("/bin/bash");
}

int main()
{
  char data [40];
  printf("Key in your answer here: ");
  fgets(data,0x40,stdin);
  
  return 0;
}
