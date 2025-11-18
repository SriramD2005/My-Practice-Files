#include <stdio.h>
typedef struct {
    float real;
    float imag;
}complex;
void swap(complex *a,complex *b){
    complex temp=*a;
    *a=*b;
    *b=temp;
}
int main(){
    complex x={1,2},y={3,4};
    printf("memory address:x:%u  y:%u\n",x,y);
    swap(&x,&y);
    printf("x:%f  y:%f",x.real,y.real);
    printf("memory address:x:%u   y:%u",x,y);
}