package week8.exception_example;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    private static Scanner s = new Scanner(System.in);

    public static void main(String[] args) {
        try {
            doSome();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private static void doSome() throws Exception{
        int num;
        try {
            num = s.nextInt();
            if (num < 0) {
                throw new NegativeException();
            }
        }
        catch (InputMismatchException | NegativeException e) {
            System.out.println("Error........");
            throw new Exception();
        }
    }
}

class NegativeException extends Exception {

}
