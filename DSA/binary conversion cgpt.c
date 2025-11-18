#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void _bin(int num, char res[]) {
    int i = 0;
    while (num > 0) {
        res[i++] = (num % 2) + '0'; // Convert digit to character
        num /= 2;
    }
    res[i] = '\0'; // Null-terminate the string
}

int binary_conversion(int num) {
    char res[40];
    _bin(num, res);
    return atoi(res); // Convert binary string back to integer
}

int main() {
    int x = binary_conversion(8);
    printf("Converted integer: %d\n", x);
    return 0;
}
