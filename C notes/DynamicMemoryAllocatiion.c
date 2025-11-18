#include <stdio.h>
#include <stdlib.h>
int main(){
    //malloc is function get the no. of bytes as input and returns the 
    //the pointer of type void pointing to the first byte of the block
    //we can access the elements of the block just like the elements of the array
    //void *ptr malloc(no.of bytes)
    char *ptr;
    ptr=(char *) malloc(3);
    for (int i=0;i<3;i++){
        ptr[0]='a';
    }
    printf("%c\n",*ptr);
    //to free the memory that we allocated for ptr we use free()
    free(ptr);
    printf("%c",*ptr);

}