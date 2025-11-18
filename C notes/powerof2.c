#include<stdio.h>
int main(){
    int x;
    scanf("%d",&x);
    int power=0;
    while(x!=1){
        if(x%2){
            printf("nope");
            break;
        }
        else{
            power++;
            x/=2;
        }

    }
    if (x==1){
        printf("yes 2 power %d",power);
    }
}