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
  char data [600];
  printf("You think you so pro now? Try me! : ");
  fgets(data,0x3000,stdin);
  
  return 0;
}
