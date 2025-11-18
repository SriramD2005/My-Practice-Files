#include <stdio.h>
int main(){
    FILE *fptr;
    fptr=fopen("practice.c","w");
    //to write in the file we fprintf()
    //fprintf(fptr,"hello world");
    fclose(fptr);
    if (fptr==NULL)printf("fptr is null after closing\n");//NOPE
    //printf("%s\n",fptr);
    FILE *fileptr;
    fileptr=fopen("practice.c","a");
    //fprintf(fileptr,"\nwritten in append mode");
    fclose(fileptr);
    //to read a data from the file we use fscanf()
    FILE *f2ptr;
    f2ptr=fopen("practice.c","r");
    char x[50];
    //fscanf(f2ptr,"%s",&x);
    //printf("%s",x);
//we can use the fgets(variable,maxsize,file pointer) to read a string from the file
    fgets(x,10,f2ptr);
    printf("%s",x);
//the functions used for files to write and read can be used for stdio too
//functions like fprintf,fscanf,fgets can be used to std if give some keywords instead of pointers to the file
    fprintf(stdout,"using the fprintf\n");
    int y;
    fprintf(stdout,"give an int value");
    fscanf(stdin,"%d",&y);
//to raise an error 
    fprintf(stderr,"\nraised error(error that I raised)\n");
    printf("after error");
}        
