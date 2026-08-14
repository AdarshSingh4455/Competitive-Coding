import java.util.Arrays;

public class BubbleSort01 {
    public static void main(String[] args) {
        int[] nums = { 12, 34, 51, 8 };
        SortAsc(nums);

        // for (int i = 0; i < nums.length; i++) {
        // System.out.println(nums[i]);
        // }
        System.out.println("In Ascending order" + Arrays.toString(nums)); // short one line method to print array..

        SortDsc(nums);
        System.out.println("In Descending order" + Arrays.toString(nums));

        SortListnew(nums);
        System.out.println("Return Array instead of only Modifying: " + Arrays.toString(nums));
    }

    public static void SortAsc(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
    }

    public static void SortDsc(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] < nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
    }

    public static int[] SortListnew(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
        return nums;
    }
}