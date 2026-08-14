public class CircularQueue {

    private int[] queue;
    private int capacity;
    private int front = 0;
    private int rear = -1;
    private int size = 0;

    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new int[capacity];
    }

    public void enqueue(int value) {
        if (size == capacity) {
            System.out.println("Queue is full!");
            return;
        }
        rear = (rear + 1) % capacity;
        queue[rear] = value;
        size++;
    }

    public int dequeue() {
        if (size == 0) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int value = queue[front];
        front = (front + 1) % capacity;
        size--;
        return value;
    }

    public int peek() {
        if (size == 0) {
            System.out.println("Queue is empty!");
            return -1;
        }
        return queue[front];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }

    public int getSize() {
        return size;
    }

    public void display() {
        if (size == 0) {
            System.out.println("Queue is empty!");
            return;
        }
        System.out.print("Queue elements: ");
        for (int i = 0; i < size; i++) {
            System.out.print(queue[(front + i) % capacity] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int capacity = 5;
        CircularQueue cq = new CircularQueue(capacity);

        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.enqueue(40);
        cq.enqueue(50);
        cq.display();

        System.out.println("Dequeued: " + cq.dequeue());
        System.out.println("Dequeued: " + cq.dequeue());
        cq.display();

        cq.enqueue(60);
        cq.enqueue(70);
        cq.display();

        System.out.println("Front element: " + cq.peek());
        System.out.println("Size: " + cq.getSize());
        System.out.println("Is Full: " + cq.isFull());
        System.out.println("Is Empty: " + cq.isEmpty());
    }
}