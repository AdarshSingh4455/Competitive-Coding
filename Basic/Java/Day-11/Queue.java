import java.util.ArrayDeque;

public class Queue{
    public static void main(String[] args) {
        java.util.Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(12);
        queue.offer(20);
        queue.offer(18);
        queue.offer(10);

        System.out.println(queue);
        int x = queue.poll();
        System.out.println(x);
        System.out.println(queue.peek());
        System.out.println(queue.isEmpty());
    }
}