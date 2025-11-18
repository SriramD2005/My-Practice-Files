#include <stdio.h>
int fact(int);
int inmaster(char x[][20]);
int main(){
    char inname[1][20];
    fgets(inname,20,stdin);
    if(inmaster(inname)){
        printf("enter the number to calculate the fact\n");
        int x;
        scanf("%d",&x);
        printf("fact of %d is %d",x,fact(x));
    }
}
int inmaster(char str[][20]){
    char master[][6]={"ragu","sriram","sanjay","rahul"};
    for (int i;i<4;i++){
        for(int j;j<6;j++){
            if(master[i][j]!=str[0][j]) break;
        }
        return 1;}
        return 0;
}
int fact(int x){
    int i=x;
    while(i!=1){
        x*=i;
        i--;
    }
    return x;
}