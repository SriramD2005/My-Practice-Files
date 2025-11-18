#include <stdio.h>
int main(){
    int *x;
    int y=2;
    x=&y;
    printf("%d",*x-1);
}
