#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void gadgetz(){
    __asm__(
        "pop %rdi;ret;"
        "pop %rsi;ret;"
        "pop %rax;ret;"
        "pop %rbx;ret;"
        "pop %rcx;ret;"
        "pop %rdx;ret;"
        "push %rdi;ret;"
        "push %rsi;ret;"
        "push %rax;ret;"
        "push %rbx;ret;"
        "push %rcx;ret;"
        "push %rdx;ret;"
        "mov %rax,(%rbx);ret;"
        "mov %rax,(%rcx);ret;"
        "mov %rax,(%rdx);ret;"
        "mov %rax,(%rdi);ret;"
        "mov %rbx,(%rax);ret;"
        "mov %rbx,(%rcx);ret;"
        "mov %rbx,(%rdx);ret;"
        "mov %rbx,(%rdi);ret;"
        "mov %rcx,(%rax);ret;"
        "mov %rcx,(%rbx);ret;"
        "mov %rcx,(%rdx);ret;"
        "mov %rcx,(%rdi);ret;"
        "syscall;"
    );

}

int main(){
    char password[512];
    memset(password, 0, 512);

    puts("What is the password? : ");
    fgets(password,0x300,stdin);

    //TODO: implement proper authentication
    puts("unauthorized!");

    return 0;
}
