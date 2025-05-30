package week4.lecture.exe3;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Employee[] employees = {
                new Employee("Keren", "R&D"),
                new Employee("Ido", "Engineering"),
                new Employee("Yuval", "IT"),
                new Employee("M", "HR")
        };

        for (Employee e : employees) {
            System.out.println(e);
        }
//        (KEr&d1001, Keren, R&D)
//        (IDing1002, Ido, Engineering)
//        (YU_it1003, Yuval, IT)
//        (_M_hr1004, M, HR)
    }
}