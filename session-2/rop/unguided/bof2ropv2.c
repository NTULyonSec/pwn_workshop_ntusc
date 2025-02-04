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
    char keyword[520];
    memset(keyword, 0, 520);

    puts("What is the secret key word? : ");
    fgets(keyword,0x300,stdin);

    return 0;
}
