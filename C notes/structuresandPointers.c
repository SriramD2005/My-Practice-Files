#include<stdio.h>
int main(){
    struct stu{
        int reg_no;
    }stu1,stu2;
    struct stu class[2]={stu1,stu2};
    struct stu *ptr;
    ptr=&stu1;
    //ptr is the pointer that can point to the variable of type struct stu
    ptr=class;//class is nothing but the pointer to the class[0]
    printf("%d \n",ptr);
    //to access the members of the structure pointed by the pointer 
    printf("%d",ptr->reg_no);//arrow operator
}