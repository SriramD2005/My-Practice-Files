//fuction prototype is used to call the function before its definition
#include <stdio.h>

void funcproto(int,int,int);//func(int k,int m); also valid
int main(){
    int x=0,y=1,z=2;
    funcproto(x,y,z);
}
void funcproto(int a,int b,int z){
    printf("x:%d,y:%d,z:%d",a,b,z);
}