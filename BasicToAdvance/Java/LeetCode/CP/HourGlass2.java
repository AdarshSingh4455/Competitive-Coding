public class HourGlass2 {
    public static void hourglassPattern(int n) {

        //Inverted triangle
        for (int i = 0; i < n; i++) {

            // spaces
            for (int j = 0; j < 2 * i; j++) {
                System.out.print(" ");
            }

            // alphabets
            for (int k = 0; k < n - i; k++) {
                System.out.print((char) ('A' + k) + " ");
            }

            System.out.println();
        }

        //Normal triangle
        for (int i = 1; i < n; i++) {

            // spaces
            for (int j = 0; j < 2 * (n - i - 1); j++) {
                System.out.print(" ");
            }

            // alphabets
            for (int k = 0; k <= i; k++) {
                System.out.print((char) ('A' + k) + " ");
            }

            System.out.println();
        }
    }
}
