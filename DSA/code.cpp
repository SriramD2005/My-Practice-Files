#include <stdio.h>
int binsearch(int ar[], int size, int x) {
    int mid, first = 0, last = size - 1;
    while (first <= last) {  // Note the change from < to <=
        mid = (first + last) / 2;
        if (ar[mid] > x)
            last = mid - 1;  // Adjust the range
        else if (ar[mid] < x)
            first = mid + 1;  // Adjust the range
        else
            return mid;  // Correctly return the index
    }
    return -1;
}
