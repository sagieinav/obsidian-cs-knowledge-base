package week2.lecture.car_exe;

public class Main {
    public static void main(String[] args) {
        Car c2 = new Car();
        c2.setCarId("12-345-67");

        for (int i = 0; i < 30; i++)
        {
            c2.accelerate();
        }

        c2.stop();

        System.out.println(c2.toString());

    }
}