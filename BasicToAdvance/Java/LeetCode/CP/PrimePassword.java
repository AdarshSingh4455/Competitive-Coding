public class PrimePassword {
    public static boolean isPrime(int a) {
        if (a < 2) {
            return false;
        }

        for (int i = 2; i <= a / i; i++) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static String generatePassword(int k) {
        if (k <= 0) {
            return "";
        }

        int num = 2;
        int count = 0;
        StringBuilder password = new StringBuilder();

        while (count < k) {
            if (isPrime(num)) {
                password.append(num);
                count++;
            }
            num++;
        }

        return password.toString();
    }

    public static void main(String[] args) {
        int k = (args.length > 0) ? Integer.parseInt(args[0]) : 10;
        System.out.println(generatePassword(k));
    }
}
