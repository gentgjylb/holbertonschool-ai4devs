// Bug 6 - Array index out of bounds
// Intended behavior: reverse an array of integers in place.

#include <iostream>
using namespace std;

void reverseArray(int arr[], int size) {
    int left = 0;
    int right = size; // BUG: should be size - 1

    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right]; // BUG: accesses arr[size] which is out of bounds
        arr[right] = temp;
        left++;
        right--;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    reverseArray(arr, size);

    // Expected output: 5 4 3 2 1
    // Actual: undefined behavior due to out-of-bounds access
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
