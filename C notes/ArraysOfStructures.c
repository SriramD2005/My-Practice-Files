#include <stdio.h>
struct labour{
    char name;
};//we can define a struct outside the main function
int main(){
    struct stud{
        int rollno;
        char name;
    };
    //instantiation
    struct stud stu1={101,'a'};
    struct stud stu2={102,'b'};
    struct stud class[]={stu1,stu2};
    printf("roll no of second student:%d\n",class[1].rollno);
    //see the difference here
    int i=0;
    printf("%c",class[++i].name);
    printf("%c",class[i++].name);
}