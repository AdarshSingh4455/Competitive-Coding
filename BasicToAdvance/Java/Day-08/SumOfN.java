public class SumOfN {
    public static void main(String[] args) {
        int n = 6;

        System.out.println(Sum_of_N(n));
    }

    public static int Sum_of_N(int n) {
        if (n == 1) {
            return 1;
        }
        return n + Sum_of_N(n - 1);
    }
}
