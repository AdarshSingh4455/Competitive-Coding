import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] nums = { 12, 15, 14, 10, 11 };

        insertion_sort(nums);
        System.out.println(Arrays.toString(nums));
    }

    public static void insertion_sort(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int key = nums[i];
            int j = i - 1;
            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
    }
}