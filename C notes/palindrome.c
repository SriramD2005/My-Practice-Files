#include <stdio.h>
int ispalindrome(char str[]){
    int i,j=0,k=0,is_palindrome=1;
    i=0;
    while (str[j]!='\0'){
        j++;
    }
    do{
        if (str[i]==str[j-1]){
            i++;
            j--;
        }
        else{
            is_palindrome=0;
            return is_palindrome;
        }
    }while (i<j);
    return is_palindrome;
}
int main(){
    int x;
    x=ispalindrome("sriram");
    printf("%d",x);
}
typedef x{
    int y;
    int z;
};
