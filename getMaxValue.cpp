#include <iostream>
using namespace std;

int findMax(int arr[], int size) {
    int max = 0;  // BUG: fails for arrays with all negative numbers

    for (int i = 0; i < size; i++) {
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

    return 0;
}
