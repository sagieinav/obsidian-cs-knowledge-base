package week5.hospital;

public class Main {

    public static void main(String[] args) {
        Hospital hospital = new Hospital("Afeka Java OOP Course");
        System.out.println("Init hospital data...");
        System.out.println(hospital.init());
        System.out.println("=== Hospital ===");
        System.out.println(hospital);
    }
}
