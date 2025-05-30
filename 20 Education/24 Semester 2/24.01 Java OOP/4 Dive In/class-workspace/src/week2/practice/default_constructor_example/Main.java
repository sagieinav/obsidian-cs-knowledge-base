package week2.practice.default_constructor_example;

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person();
        System.out.println("p1: " + p1);

        Person p2 = new Person("207456047", "Sagi");
        System.out.println("p2: " + p2);
    }
}
