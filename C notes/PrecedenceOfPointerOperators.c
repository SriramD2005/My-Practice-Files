#include<stdio.h>
#include<stdlib.h>
int main(){
    struct stu{
        int rollno;
    }stu1,stu2;
    struct stu class[]={stu1,stu2};
    //precedance order:
      //->
      //.
      //++
      //*etc
    struct stu *ptr;
    printf("%d",ptr->rollno);//same as (*ptr).rollno
    //but
    //printf("%d",*ptr.rollno) will be an error as '.' has more precedence than '*'
}