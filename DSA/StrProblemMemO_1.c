#include <stdio.h>
#include <stdlib.h>
char* Format(char*, int);
int main(){
    
    char a[]  = "aabcccccaaa";
    char* str = Format(a, 11);
    printf("%s", str);
    free(str);
}
char* Format(char* a, int length){
    int count = 1, aP = 0;
    int i;
    for (i = 1; i<length; i++){
        if (a[i] == a[aP]){
            count++;
        }
        else{
            a[++aP] = count +'0';
            a[++aP] = a[i];
            count = 1;
        }
    }
    printf("%d",aP);
    a[aP] = a[i-1];
    a[++aP] = count+'0';
    return a;
}