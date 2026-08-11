import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class stockSpan {

    static class Pair {
        int price;
        int span;

        Pair(int price, int span) {
            this.price = price;
            this.span = span;
        }
    }

    public static int[] stock_Span(int[] prices) {

        int n = prices.length;
        int[] result = new int[n];

        Deque<Pair> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {

            int price = prices[i];
            int span = 1;

            while (!stack.isEmpty() &&
                   stack.peek().price <= price) {

                Pair previous = stack.pop();

                span += previous.span;
            }

            stack.push(new Pair(price, span));

            result[i] = span;
        }

        return result;
    }

    public static void main(String[] args) {

        int[] prices = {100, 80, 60, 70, 60, 75, 85};

        int[] result = stock_Span(prices);

        System.out.println(Arrays.toString(result));
    }
}