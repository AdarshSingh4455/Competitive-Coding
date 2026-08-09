import java.util.ArrayDeque;
import java.util.Deque;

public class Stack{
    public static void main(String[] args) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(12);
        stack.push(13);
        stack.push(14);
        stack.push(16);
        System.out.println(stack);
        System.out.println("See top element before deletion : " + stack.peek());
        System.out.println("Popped top element : " + stack.pop());
        System.out.println("See top element after deletion : " + stack.peek());
        System.out.println("Check stack is empty or not : " + stack.isEmpty());
        System.out.println("Check size of stack : " + stack.size());
        System.out.println(stack);
    }
}