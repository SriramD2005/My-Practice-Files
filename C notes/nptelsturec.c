#include <stdio.h>
struct student{
    int rollno;
    char name[30];
    int mark;
};
void sort(struct student array[],int len);
int main(){
    int nstu;
    scanf("%d",&nstu);
    struct student stu_arr[nstu];
    for (int i=0;i<nstu;i++){
        printf("rollno");
        scanf("%d",&stu_arr[i].rollno);
        printf("name");
        scanf("%s",&stu_arr[i].name);
        printf("marks:");
        scanf("%d",&stu_arr[i].mark);
    }
   sort(stu_arr,nstu);
   for (int i=0;i<nstu;i++){
    printf("hi");
    printf("rollno:%d\n",stu_arr[i].rollno);
    printf("name:%s\n",stu_arr[i].name);
    printf("marks:%d\n",stu_arr[i].mark);
   } 
}
void sort(struct student array[],int len){
    for (int i=0;i<len;i++){
        for (int j=0;j<len-i-1;j++){
            if (array[j].mark>array[j+1].mark){
                struct student temp=array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
    }
}