import java.util.Arrays;

public class Sample {

    public static void main(String[] args) {
        int[] array = {12, 5, 23, 42, 8, 3};
        int[] indices = mergeSortIndices(array);

        System.out.println("Original Array: " + Arrays.toString(array));
        System.out.println("Sorted Indices: " + Arrays.toString(indices));
    }

    private static int[] mergeSortIndices(int[] array) {
        int n = array.length;
        int[] indices = new int[n];

        // Initialize indices with the values from 0 to n-1
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }

        mergeSort(array, indices, 0, n - 1);

        return indices;
    }

    private static void mergeSort(int[] array, int[] indices, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            // Recursively sort the left and right halves
            mergeSort(array, indices, left, mid);
            mergeSort(array, indices, mid + 1, right);

            // Merge the sorted halves
            merge(array, indices, left, mid, right);
        }
    }

    private static void merge(int[] array, int[] indices, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        // Copy data to temporary arrays
        for (int i = 0; i < n1; ++i) {
            leftArray[i] = indices[left + i];
        }
        for (int j = 0; j < n2; ++j) {
            rightArray[j] = indices[mid + 1 + j];
        }

        // Merge the temporary arrays
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (array[leftArray[i]] <= array[rightArray[j]]) {
                indices[k] = leftArray[i];
                i++;
            } else {
                indices[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of leftArray, if any
        while (i < n1) {
            indices[k] = leftArray[i];
            i++;
            k++;
        }

        // Copy remaining elements of rightArray, if any
        while (j < n2) {
            indices[k] = rightArray[j];
            j++;
            k++;
        }
    }
}

