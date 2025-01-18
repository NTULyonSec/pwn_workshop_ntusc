#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void power() {
  system("/bin/sh");
}

void vuln(){
	char buf[256];
	printf("\nSo what's your name again?: ");
	scanf("%s",buf);
	printf("Hi %s, thanks for letting me know your name. I hope I remember it the next time you talk to me.",buf);
	fflush(stdout);
}

int main(int argc, char *argv[]) {
  setbuf(stdin,NULL);
  setbuf(stdout,NULL);
  setbuf(stderr, NULL);
  vuln();

  return 0;
}
