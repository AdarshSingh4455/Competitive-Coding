import java.util.HashSet;

public class DuplicateandMissing {
    public static void findDuplicateAndMissing(int[] arr, int n) {
        HashSet<Integer> set = new HashSet<>();
        for(int i=0;i<arr.length;i++){
            if (!set.add(arr[i])) {
                System.out.println("Duplicate: " + arr[i]);
            }
        }
        System.out.println(set);

        for(int i=1;i<=n;i++){
            if (!set.contains(i)) {
                System.out.print("Missing: "+ i);
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1,2,3,2,4};
        findDuplicateAndMissing(arr, 5);
    }
}
