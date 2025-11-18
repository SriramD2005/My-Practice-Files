#include <stdio.h>
int main(){
    int *pointer;//that is pointer can point to the variable 
                 //of type int
    int x=2;
    //*pointer=&x;throws an error. therefore use * star only for the declaration of pointer
    pointer=&x;//both are legal
    printf("memory address: %d/n",pointer);
    int y;
    y=pointer;//pointer has the memory location of x that is what assigned to y
    printf("without using indirection operator(*):");
    printf("%d\n",y);
    //if you wanna assign the value of the variable that the pointer pointing to you must use indirection operator(*)
    y=*pointer;
    printf("using indirection operator(*):");
    printf("%d\n",y);
    y=*&x;//equivalent to y=x;
    //int z=&x;
    //printt("%d",*z); invalid statement
}