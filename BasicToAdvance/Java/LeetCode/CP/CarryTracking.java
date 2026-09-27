import java.util.Scanner;

public class CarryTracking {

    // public static int countCarry(int a, int b) {
    //     int count = 0;
    //     int carry = 0;

    //     while (a > 0 || b > 0) {

    //         int x = a % 10;
    //         int y = b % 10;

    //         int sum = x + y + carry;

    //         if (sum > 9) {
    //             carry = 1;
    //             count++;
    //         } else {
    //             carry = 0;
    //         }

    //         a = a / 10;
    //         b = b / 10;
    //     }

    //     return count;
    // }
    public static int countCarry(int a, int b) {
        int count = 0;
        int carry = 0;

        while (a > 0 || b > 0) {
            int x = a % 10;
            int y = b % 10;

            int sum = x + y + carry;

            carry = sum / 10;

            if (carry == 1) {
                count++;
            }

            a /= 10;
            b /= 10;
        }

        return count;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        int result = countCarry(a, b);

        System.out.println("Number of carries: " + result);

        sc.close();
    }
}