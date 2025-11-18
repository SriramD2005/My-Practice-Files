#include <stdio.h>
int bin(int);
int main(){
    printf("%d",bin(8));
}
int bin(int num){
    int bin=0;
    int mult=1;
    while(num/2!=1){
        bin+=num%2*mult;
        num/=2;
        mult*=10;
    }
    if (num/2==1){
        bin+=1*mult*10;
    }  
    return bin; 
}