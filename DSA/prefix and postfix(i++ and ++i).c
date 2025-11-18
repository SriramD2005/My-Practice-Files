#include <stdio.h>
int main(){
    int x=1;
    int m;
    m=x++;
    printf("m:%d",m);
    x=0;
    m=++x;
    printf("m:%d",m);
    return 0;
}