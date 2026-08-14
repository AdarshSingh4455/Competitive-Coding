public class PriorityQueue {
    public static void main(String[] args) {
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>();
        pq.offer(10);
        pq.offer(20);
        pq.offer(30);
        pq.offer(40);

        System.out.println(pq);
        System.out.println(pq.poll());
        System.out.println(pq.peek());
        System.out.println(pq);
    }
}