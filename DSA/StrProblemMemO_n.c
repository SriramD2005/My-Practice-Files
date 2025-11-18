#include <stdio.h>
#include <stdlib.h>
char* Format(char*, int);
int main(){
    
    char a[]  = "aabcccccaaa";
    int lenth = sizeof(a)/sizeof(char);
    char* str = Format(a, 11);
    printf("%s", str);
    free(str);
}
char* Format(char* a, int length){
    int count = 1, aP = 0;
    char* res = (char*) malloc(sizeof(char)*length);
    res[0] = a[0];
    int i;
    for (i = 1; i<length; i++){
        if (a[i] == res[aP]){
            count++;
        }
        else{
            res[++aP] = count +'0';
            res[++aP] = a[i];
            count = 1;
        }
    }
    i = 0;
    i =i++;
    printf("%d\n",i);
    printf("%c\n",res[aP]);
    res[++aP] = count + '0';
    return res;
}