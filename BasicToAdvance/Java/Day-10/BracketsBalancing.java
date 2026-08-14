public class BracketsBalancing {
    public static void main(String[] args) {
        
    }

    public static boolean balance_brackets(String s){
        java.util.Stack<Character> stack = new java.util.Stack<>();
        char[] pairs = {
            ')', '(',
            '}', '{',
            ']', '['
        };
        
        for(char c : s.toCharArray()){
            if(c == '(' || c == '{' || c == '['){
                stack.push(c);
            } else if(c == ')' || c == '}' || c == ']'){
                if(stack.isEmpty()) return false;
                char top = stack.pop();
                if(!isMatching(top, c)) return false;
            }
        }
        
        return stack.isEmpty();
    }
    
    private static boolean isMatching(char open, char close){
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
    }
}
