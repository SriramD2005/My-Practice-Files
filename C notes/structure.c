#include <stdio.h>
int main(){
    struct class{
        int room_no;
        char name[20];
        char dept[20];
    };
    struct class aids;
    aids.room_no=205;
    aids.name[10]={'2','n','d'};
    printf("%d, %s",aids.room_no,aids.name);
}