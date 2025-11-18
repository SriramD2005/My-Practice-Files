#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node* next;
};
//to count number of nodes in a list
int len(struct node* head){
    int count;
    if (head) count=1;else return 0;
    while (head){
        count++;
        head=head->next;
    }return count;
    }
    //we pass the pointer to the pointer of the head node because we are not going to update the head structure we want to update the value of pointer itself
void insertAtFirst(struct node** head,int data){
    //we allocate the memory dynamically so that the new node exist even after the 
    //after the function ends. usually all the memory allocated by the compiler
    //will be released when the function ends.
    struct node* new=(struct node*) malloc(sizeof(struct node));
    new->data=data;
    new->next=*head;//this returns the pointer to the head not the actual structure that the head points
    *head=new;
}
void printlist(struct node* head){
    struct node* current=head;
    while(current){
        printf("%d->",current->data);
        current=current->next;
    }printf("NULL\n");
}
void deletenode(struct node **head,int index);
int main(){
    struct node* head=NULL;
    insertAtFirst(&head,1);
    insertAtFirst(&head,2);
    printlist(head);
    deletenode(&head,1);
    printlist(head);
}
void deletenode(struct node** head,int index){
    int count=0;
    struct node* current=*head;
    while (count<index-1){
        count++;
        current=current->next;
    }
    struct node* delnode=current->next;
    current->next=current->next->next;
    free(delnode);//the free() function clear the data stored in the memory space pointed by the pointer which was passed argument
}
