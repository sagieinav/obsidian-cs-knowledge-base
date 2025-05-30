package week7.vehicle_exercise;

import week7.vehicle_exercise.vehicle_types.Car;
import week7.vehicle_exercise.vehicle_types.Motorcycle;
import week7.vehicle_exercise.vehicle_types.Truck;

public class Main {
    public static void main(String[] args) {
        Garage garage = new Garage();

        Vehicle vehicle = new Vehicle("144-23-175", 2018, 100.0);
        Vehicle car = new Car("123-45-678", 2020, 180.0);
        Vehicle motorcycle = new Motorcycle("987-65-432", 2022, 220.0);
        Vehicle truck = new Truck("555-66-777", 2018, 140.0);

        garage.addVehicle(vehicle);
        garage.addVehicle(car);
        garage.addVehicle(motorcycle);
        garage.addVehicle(truck);

        System.out.println("Starting drive:");
        garage.driveAll();
    }
}
