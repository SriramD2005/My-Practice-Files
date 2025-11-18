#include <stdio.h>
int main(){
    int x;
    int sum=0;
    scanf("%d",&x);
    for (int i=1;i<=(int)(x/2);i++){
        if (!(x%i))sum+=i;
    }
    printf("%d",sum);
    if (x==sum) printf("%d is perfect",x);
}