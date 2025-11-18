#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(){
    char str[50];
    fgets(str,50,stdin);
    int uc=0,lc=0;
    for (int i=0;i<strlen(str);i++){
        if (isupper(str[i]))uc++;
        if (islower(str[i]))lc++;
    }
    printf("no. of upper case:%d\n",uc);
    printf("no. of lower case:%d",lc);
}