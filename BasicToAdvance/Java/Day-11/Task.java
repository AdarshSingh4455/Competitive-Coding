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

    @Override
    public int compareTo(Task other){
        int priorityResult = Integer.compare(this.priority, other.priority);
        if (priorityResult != 0){
            return priorityResult;
        }
        return Integer.compare(this.sequence, other.sequence);
    }
}
