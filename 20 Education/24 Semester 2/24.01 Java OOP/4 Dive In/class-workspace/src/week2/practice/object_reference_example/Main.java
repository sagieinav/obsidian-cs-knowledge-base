package week2.practice.object_reference_example;

public class Main {
    public static void main(String[] args) {
        Car[] cars = new Car[3];
        cars[0] = new Car("Honda", 2016);
        cars[1] = new Car("Honda", 2018);
        cars[2] = new Car("BMW", 2017);
        cars = copy(cars, cars.length * 2);
        cars[3] = new Car("Mazda", 2015);
        System.out.println("After init:");
        System.out.println(str(cars));
        Car firstCar = cars[0]; // Shallow copy. point to the same address.
        Car secondCar = new Car(cars[1]); // Deep copy. copy the value into a new variable.
        System.out.println("First car (before change): " + firstCar);
        firstCar.setYear(2017);
        firstCar.setModel("Honda Civic");
        System.out.println("First car (after change): " + firstCar);
        System.out.println("After change:");
        System.out.println(str(cars));

    }

    private static String str(Object[] arr) { // Convert array to String
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < arr.length; i++){
            sb.append(arr[i]);
            if (i != arr.length - 1){
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }


    private static Car[] copy(Car[] cars, int size){
        Car[] new_arr = new Car[size];
        for (int i = 0; i < cars.length; i++){
            new_arr[i] = cars[i];
        }
        return new_arr;
    }
}



class Car{
    private String model;
    private int year;

    public Car(String model, int year) {
        setModel(model);
        setYear(year);
    }

    public Car(Car other){
        this.model = other.model;
        this.year = other.year;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public String toString() {
        return "(" + model + ", " + year + ")";
    }
}