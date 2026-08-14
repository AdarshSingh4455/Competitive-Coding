import java.util.PriorityQueue;

public class TaskScheduler{
    public static void main(String[] args) {
        PriorityQueue<Task> pq = new PriorityQueue<>();

        pq.offer(new Task(2,0,"A"));
        pq.offer(new Task(1,1,"B"));
        pq.offer(new Task(2,3,"C"));

        while (!pq.isEmpty()) {
            Task task = pq.poll();

            System.out.println(task.getName());
        }
    }
}