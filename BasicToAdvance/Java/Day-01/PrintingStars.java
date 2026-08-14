public class PrintingStars {

    public static void main(String[] args) {
        int n = 5; // Number of rows

        for (int i = 1; i <= n; i++) {
            // Print spaces
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println(); // Move to the next line
        }

        for (int k = 1; k <= n; k++) {
            for (int i = n; i >= k; i--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}