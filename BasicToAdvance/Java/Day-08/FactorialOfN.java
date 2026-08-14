public class FactorialOfN {
    public static void main(String[] args) {
        int n = 5;

        System.out.println(Nfactorial(n));

    }

    public static int Nfactorial(int n) {
        if (n == 1) {
            return 1;
        }
        return n * Nfactorial(n - 1);
    }
}