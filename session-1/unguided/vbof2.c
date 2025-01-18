#include <stdio.h>
#include <stdlib.h>

int win()
{
system("/bin/sh");
}

int main()
{
  char data [0x100];
  printf("Nyehehe I'm back. What's the password?: ");
  fgets(data,0x1000,stdin);
  
  return 0;
}
