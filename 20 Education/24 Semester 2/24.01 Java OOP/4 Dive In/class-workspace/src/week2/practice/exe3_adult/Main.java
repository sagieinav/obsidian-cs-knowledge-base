package week2.practice.exe3_adult;

public class Main {
    public static void main(String[] args) {
        Adult a1 = new Adult("Sagi", "pro", 174);
        System.out.println(a1);
        Adult a2 = new Adult("Yossi", 189);
        System.out.println(a2);
        Adult a3 = new Adult("Moshe", 245);
        System.out.println(a3);
        Adult a4 = new Adult("Avi", 245);
        System.out.println(a4);
        Adult a5 = new Adult(a2);
        System.out.println(a5);
        a2.setHeight(122);
        System.out.println(a5);
    }
}
