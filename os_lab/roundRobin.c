#include <stdio.h>
#include <stdlib.h>
typedef struct process{
    int id;
    int bt;
    int rt;//remaining time
    int wt;
    int tat;
}process;
void round_robin(process ps[], int quantum){
    int done;
    int time=0;
    while(1){
        done = 1;
        for (int i = 0;i<5;i++){
            if (ps[i].rt){
                done = 0;
                if(ps[i].rt>quantum){
                    ps[i].rt-=quantum;
                    time+=quantum;
            }
            else{
                time = time + ps[i].rt;
                ps[i].rt = 0;
                ps[i].wt = time - ps[i].bt;
                ps[i].tat = time;
            }

        }
    }
    if (done) break;
}}
void main(){
    process ps[5] = {{1, 10, 10, 0, 0},
    {2, 5, 5, 0, 0},
    {3, 8, 8, 0, 0},
    {4, 6, 6, 0, 0},
    {5, 4, 4, 0, 0}};
    round_robin(ps, 4);
    printf("%d",ps[0].wt);
}