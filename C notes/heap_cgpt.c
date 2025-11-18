#include<stdio.h>
#include<stdlib.h>
void percup(int heap[], int i) {
    int curr = i - 1; // Adjust index to 0-based
    while (curr > 0) {
        int parentIndex = (curr - 1) / 2;
        if (heap[parentIndex] < heap[curr]) {
            int temp = heap[curr];
            heap[curr] = heap[parentIndex];
            heap[parentIndex] = temp;
        } else {
            break;
        }
        curr = parentIndex;
    }
}
void percdown(int heap[], int* length) {
    int curr = 0; // Start at the root
    while (curr < *length / 2) { // Only process non-leaf nodes
        int child1Index = 2 * curr + 1; // Left child index
        int child2Index = 2 * curr + 2; // Right child index
        int maxIndex = curr; // Assume the current node is the largest

        // Compare with the left child
        if (child1Index < *length && heap[child1Index] > heap[maxIndex]) {
            maxIndex = child1Index;
        }

        // Compare with the right child
        if (child2Index < *length && heap[child2Index] > heap[maxIndex]) {
            maxIndex = child2Index;
        }

        // If the current node is already the largest, stop
        if (maxIndex == curr) {
            break;
        }

        // Swap the current node with the largest child
        int temp = heap[curr];
        heap[curr] = heap[maxIndex];
        heap[maxIndex] = temp;

        // Move to the largest child
        curr = maxIndex;
    }
}

int popmax(int heap[], int* length) {
    if (*length <= 0) {
        return -1; // Return -1 if the heap is empty
    }
    int max = heap[0];
    heap[0] = heap[--(*length)];
    percdown(heap, length);
    return max;
}

int main() {
    int size;
    scanf("%d", &size); // Removed trailing space
    int heap[size];
    for (int i = 0; i < size; i++) {
        scanf("%d", &heap[i]); // Removed trailing space
        percup(heap, i + 1);
    }

    int hlength = size;
    int n;
    scanf("%d", &n); // Removed trailing space
    for (int j = 0; j < n; j++) {
        printf("%d ", popmax(heap, &hlength));
    }
    return 0;
}