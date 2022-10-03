public class Zero {

    public static void main(String[] args) {
        int numerator = 10;
        int denominator = 0;
        try {
            System.out.println(numerator / denominator);
            System.out.println("This text will not be printed.");
        } catch (ArithmeticException e) {
            System.out.println(e);
        }
    }
}
