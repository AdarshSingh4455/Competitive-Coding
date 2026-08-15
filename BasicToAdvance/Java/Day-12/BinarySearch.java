public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {12,18,26,30,45,62};
        int target = 30;

        int x = binarySearch(arr,target);
        System.err.println(x);
    }

    public static int binarySearch(int[] arr, int target){
        int n = arr.length;
        int high = n-1;
        int low = 0;

        while (low<=high) {
            int mid = (low + high)/2;
            if (arr[mid]==target) {
                return mid;
            }else if (arr[mid]<target) {
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return -1;
    }
}
