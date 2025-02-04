#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln()
{
  __asm__(
   "call %rsp;"
  );
}

int main()
{
  char data [3000];
  printf("It's me again! What do you have to say for yourself? : ");
  fgets(data,0x3000,stdin);
  
  return 0;
}
