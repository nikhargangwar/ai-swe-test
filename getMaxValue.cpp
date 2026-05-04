#include <iostream>
using namespace std;

int findMax(int arr[], int size) {
    // Check if the array is empty to prevent out-of-bounds access.
    if (size <= 0) {
        // Return an appropriate value or throw an exception for an empty array.
        // For this fix, we'll return 0, assuming that is a reasonable default.
        // However, for a more robust solution, consider throwing an exception.
        return 0; 
    }

    int max = arr[0];  // FIX: Initialize max with the first element to handle negative numbers correctly.

    for (int i = 1; i < size; i++) { // Start loop from the second element as arr[0] is already assigned to max.
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    return max;
}

int main() {
    int arr[] = {-10, -20, -3, -40};
    int size = 4;

    int result = findMax(arr, size);
    cout << "Maximum value is: " << result << endl;

    // Test case with positive numbers
    int arr2[] = {10, 20, 3, 40};
    int size2 = 4;
    result = findMax(arr2, size2);
    cout << "Maximum value is: " << result << endl;

    // Test case with mixed numbers
    int arr3[] = {-10, 20, -3, 40};
    int size3 = 4;
    result = findMax(arr3, size3);
    cout << "Maximum value is: " << result << endl;

    // Test case with single element
    int arr4[] = {-5};
    int size4 = 1;
    result = findMax(arr4, size4);
    cout << "Maximum value is: " << result << endl;

    // Test case with empty array
    int arr5[] = {};
    int size5 = 0;
    result = findMax(arr5, size5);
    cout << "Maximum value is: " << result << endl;

    return 0;
}
