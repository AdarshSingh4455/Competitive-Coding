import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] arr = { 12, 34, 10, 21, 18 };

        int[] res = mergeSort(arr);

        System.out.println(Arrays.toString(res));
    }

    public static int[] mergeSort(int[] arr) {
        int n = arr.length;

        if (n <= 1) {
            return arr;
        }
        int mid = n / 2;

        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, n);

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    public static int[] merge(int[] left, int[] right) {
        int i = 0;
        int j = 0;
        int[] result = new int[left.length + right.length];
        int k = 0;

        while (left.length > i && right.length > j) {
            if (left[i] < right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }

        while (left.length > i) {
            result[k++] = left[i++];
        }

        while (right.length > j) {
            result[k++] = right[j++];
        }

        return result;
    }
}