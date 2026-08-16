public class FirstOccurance {
    public static void main(String[] args) {
        int[] arr = {12,18,26,26,45,62};
        int target = 26;

        int x = binarySearch(arr,target);
        System.out.println(x);
    }

    public static int binarySearch(int[] arr, int target){
        int answer = -1;
        int n = arr.length;
        int high = n-1;
        int low = 0;

        while (low<=high) {
            int mid = (low + high)/2;
            if (arr[mid]==target) {
                answer = mid;
                high = mid-1;
            }else if (arr[mid]<target) {
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return answer;
    }
}
