import java.util.Arrays;

public class PackageDelivery {
    public static void main(String[] args) {
        int[] packages = {2 , 3 , 5 , 7 , 9};
        int days = 3;

        System.out.println(ship_within(packages, days));
    }

    public static boolean can_do(int[] packages, int capacity, int days){
        int used_days = 1;
        int current_weight = 0;
        for (int i = 0; i < packages.length; i++) {
            if (packages[i] + current_weight <= capacity) {
                current_weight += packages[i];
            }else{
                used_days += 1;
                current_weight = packages[i];
            }
        }
        return used_days<=days;
    }

    public static int ship_within(int[] packages, int days){
        int low = Arrays.stream(packages).max().getAsInt();
        int high = Arrays.stream(packages).sum();
        int answer = high;

        while (low<=high) {
            int mid = (low + high)/2;
            if (can_do(packages, mid, days)) {
                answer = mid;
                high = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        return answer;
    }
}
