public class Hourglass{
    public static void hourglassPattern(int n) {

        for (int i = 0; i < 2 * n - 1; i++) {

            int spaces;
            int chars;

            if (i < n) {
                // Upper half
                spaces = 2 * i;
                chars = n - i;
            } else {
                // Lower half
                spaces = 2 * (2 * n - 2 - i);
                chars = i - n + 2;
            }

            // Print spaces
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }

            // Print A, B, C...
            for (int k = 0; k < chars; k++) {
                System.out.print((char) ('A' + k) + " ");
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {
        hourglassPattern(5);
    }
}