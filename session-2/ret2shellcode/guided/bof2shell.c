#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln()
{
  __asm__(
   "jmp %rsp;"
  );
}

int main()
{
  char data [1024];
  printf("It's me again! What do you have to say for yourself? : ");
  fgets(data,0x1000,stdin);
  
  return 0;
}
