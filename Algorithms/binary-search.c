#include <stdio.h>

/**/
int binary_search(int arr[], int length, int target) {
  int low = 0, high = length - 1;

  while (low <= high) {
    int mid = low + (high - low) / 2;
    int mid_element = arr[mid];

    if (mid_element == target) {
      return mid;
    } else if (mid_element < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
}

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int length = sizeof(arr) / sizeof(arr[0]);
  int target = 7;

  int result = binary_search(arr, length, target);

  if (result != -1) {
    printf("Element %d found at index %d.\n", target, result);
  } else {
    printf("Element %d not found.\n", target);
  }

  return 0;
}
