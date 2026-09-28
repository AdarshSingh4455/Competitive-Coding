public class ReverseWordWithLength {

    public static String reverseWords(String str) {

        String[] words = str.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {

            int length = word.length();

            String reverse = new StringBuilder(word)
                    .reverse()
                    .toString();

            result.append(length);
            result.append(reverse);
            result.append(" ");
        }

        return result.toString().trim();
    }

    public static void main(String[] args) {

        String str = "hello i am adarsh";

        System.out.println(reverseWords(str));
    }
}