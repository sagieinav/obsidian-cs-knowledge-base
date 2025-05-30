package week3.lecture.rectangle_exe;

public class Main {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle();
        System.out.println(r1);
        System.out.println("Perimeter: " + r1.getPerimeter());
        System.out.println("Area: " + r1.getArea());
        System.out.println(r1.showByChar('#'));
    }
}
