import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

public class NextGreater {
    public static void main(String[] args) {
        int[] arr = {7,3,5,12,8};

        int[] result = next_greater_element(arr);
        System.out.println(Arrays.toString(result));
    }

    public static int[] next_greater_element(int[] arr){
        Deque<Character> stack = new ArrayDeque<>();
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);

        for(int i=n-1;i>=0;i--){
            int current = arr[i];
            while (!stack.isEmpty() && stack.peek()<=current) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                result[i] = stack.peek();
            }
            stack.push((char) current);
        }
        return result;
    }
}
