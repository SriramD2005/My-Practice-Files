#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//#include <sys/wait.h>
#include <fcntl.h>
int main(){
    int x = 2;
    printf("%d",x);
    pid_t pid = fork();
    printf("%d",pid);
}