#include <stdio.h>
int main(){
    char str[10];
    fgets(str, 10, stdin);
    for (int i = 0; i < 10; i++){
        if (str[i] < 92 && str [i] > 64){
            printf("Caps\n");
        }
        else printf("Small\n");
    }

}