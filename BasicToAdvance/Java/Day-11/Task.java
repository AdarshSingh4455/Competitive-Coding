public class Task implements Comparable<Task> {
    private final int priority;
    private final int sequence;
    private final String name;

    public Task(int priority, int sequence, String name){
        this.priority = priority;
        this.sequence = sequence;
        this.name = name;
    }

    public int getPriority(){
        return priority;
    }

    public int getSequence(){
        return sequence;
    }

    public String getName(){
        return name;
    }

    public static void main(String[] args) {
        Task task1 = new Task(1, 2, "Write code");
        Task task2 = new Task(1, 1, "Review code");

        System.out.println(task1.compareTo(task2));
    }

    @Override
    public int compareTo(Task other){
        int priorityResult = Integer.compare(this.priority, other.priority);
        if (priorityResult != 0){
            return priorityResult;
        }
        return Integer.compare(this.sequence, other.sequence);
    }
}
