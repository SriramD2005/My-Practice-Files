#include<stdio.h>
#include<stdlib.h>

void percup(int heap[], int i) {
    int curr = i - 1; // Adjust index to 0-based
    while (curr >= 0) {
        int* parent = &heap[(int)((curr - 1) / 2)]; // Pointer to the parent node
        if (*parent < heap[curr]) {
            int temp = heap[curr];
            heap[curr] = *parent;
            *parent = temp;
        } else {
            break;
        }
        curr = (int)((curr - 1) / 2); // Move to the parent node
    }
}

void percdown(int heap[], int* length) {
    int curr = 0;
    while (curr <= *length - 1) { // Process nodes until the last non-leaf node
        int* child1 = &heap[(int)((2 * curr) + 1)]; // Pointer to the left child
        int* child2 = &heap[(int)((2 * curr) + 2)]; // Pointer to the right child

        if ((2 * curr + 1) > *length - 1) { // If left child is out of bounds
            break;
        }

        if ((2 * curr + 2) <= *length - 1) { // If right child exists
            if (*child1 <= *child2) { // Compare left and right children
                int temp = *child2;
                *child2 = heap[curr];
                heap[curr] = temp;
                curr = (int)((2 * curr) + 2); // Move to the right child
            } else {
                int temp = *child1;
                *child1 = heap[curr];
                heap[curr] = temp;
                curr = (int)((2 * curr) + 1); // Move to the left child
            }
        } else { // Only left child exists
            int temp = *child1;
            *child1 = heap[curr];
            heap[curr] = temp;
            curr = (int)((2 * curr) + 1); // Move to the left child
        }
    }
}

int popmax(int heap[], int* length) {
    if (*length <= 0) {
        return -1; // Return -1 if the heap is empty
    }
    int max = heap[0]; // The maximum element is at the root
    heap[0] = heap[--(*length)]; // Replace the root with the last element
    percdown(heap, length); // Restore the heap property
    return max;
}

int main() {
    int size;
    scanf("%d", &size); // Read the size of the heap
    int heap[size];
    for (int i = 0; i < size; i++) {
        scanf("%d", &heap[i]); // Read the elements of the heap
        percup(heap, i + 1); // Insert each element into the heap
    }

    int* hlength;
    int l = size;
    hlength = &size; // Pointer to the size of the heap

    int n;
    scanf("%d", &n); // Read the number of elements to extract
    for (int j = 0; j < n; j++) {
        printf("%d ", popmax(heap, hlength)); // Extract and print the maximum element
    }
    return 0;
}