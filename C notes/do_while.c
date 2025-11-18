#include <stdio.h>
int main(){
    int x = 2;
    int i = 0;
    //while(x==2); if this statement is executed nothing after this will be executed.
    do{
        printf("hi");
        i++;
        while(x==2);//the following statements will not be executed untill the while's condition fails.
        printf("yes");
    }while(i<=3);
}