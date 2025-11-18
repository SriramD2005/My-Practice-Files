#include <stdio.h>
int main(){
    //without using the structure name hence we cant use it again
    struct {
        int x;
    }ins;
    ins.x=2;
    printf("%d",ins.x);
    //to make it useful for future requirements
    struct structure{
        int y;
    }ins2;
    ins2.y=3;
    
}