#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int _bin(int num,char a[]);
int binary_conversion(int num){
    char res[40];
    return _bin(num,res);
}
int _bin(int num,char res[100]){
    if (num/2==1) return res;
    int x;
    x=num%2;
    (char)x;
    strcat(res,x);
}
int main(){
    int x=atoi(binary_conversion(8));
    printf("%d",x);}