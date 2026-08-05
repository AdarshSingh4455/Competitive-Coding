import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = { 12, 15, 10, 20, 8 };

        SelectionSortAsc(arr);
        System.out.println("Array sorted using Selection Sort: " + Arrays.toString(arr));
    }

    public static void SelectionSortAsc(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
}
