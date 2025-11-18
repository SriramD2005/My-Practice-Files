#include <stdio.h>
typedef struct process{
    int id;
    int bt;
    int rt;//remaining time
    int wt;
    int tat;
}process;
void round_robin(process ps[], int n, int quantum) {
    int time = 0; // Initialize time
    int done;

    while (1) {
        done = 1; // Assume all processes are done

        for (int i = 0; i < n; i++) {
            if (ps[i].rt > 0) {
                done = 0; // There is at least one process left

                if (ps[i].rt > quantum) {
                    // Process requires more than one quantum
                    time += quantum;
                    ps[i].rt -= quantum;
                } else {
                    // Process can finish in this quantum
                    time += ps[i].rt;
                    ps[i].wt = time - ps[i].bt; // Waiting time = total time - burst time
                    ps[i].rt = 0;              // Process is done
                    ps[i].tat = time;          // Turnaround time = total time
                }
            }
        }

        if (done) {
            break; // Exit the loop if all processes are done
        }
    }
}
int main(){
    process ps[5] = {{1, 10, 10, 0, 0},
    {2, 5, 5, 0, 0},
    {3, 8, 8, 0, 0},
    {4, 6, 6, 0, 0},
    {5, 4, 4, 0, 0}};
    round_robin(ps, 4);
    printf("%d",ps[0].wt,4);
}