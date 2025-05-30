package week10.shapes_exe;

import week7.shapes_exercise.COLORS;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException {
        Supplier s1 = new Supplier("Ori",
                new Address("Ramat", "Ben", "25"));
        Supplier s2 = new Supplier("Gefen",
                new Address("Levanon", "Nasaralla", "65"));
        Shape[] shapes = {
                new Circle(2, COLORS.BLACK, 2.5, s1),
                new Square(3, COLORS.BLACK, 4, s2)
        };
        System.out.println(Arrays.toString(shapes));
        Shape[] shapes2 = Arrays.copyOf(shapes, shapes.length);
        shapes2[1].setColor(COLORS.BLUE);
        System.out.println("After change....");
        System.out.println(Arrays.toString(shapes));
        System.out.println(Arrays.toString(shapes2));
        System.out.println("After using clone");
        shapes2 = new Shape[shapes.length];
        for (int i = 0; i < shapes.length; i++) {
            shapes2[i] = shapes[i].clone();
        }
        shapes2[1].setColor(COLORS.GREEN);
        System.out.println("After change....");
        System.out.println(Arrays.toString(shapes));
        System.out.println(Arrays.toString(shapes2));
    }
}
