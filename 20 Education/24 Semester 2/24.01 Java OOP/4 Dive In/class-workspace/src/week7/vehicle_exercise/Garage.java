package week7.vehicle_exercise;

import week7.vehicle_exercise.vehicle_types.Car;
import week7.vehicle_exercise.vehicle_types.Motorcycle;
import week7.vehicle_exercise.vehicle_types.Truck;

import java.util.Arrays;

public class Garage {
    private Vehicle[] vehicles = new Vehicle[1];
    private int numOfVehicles;

    public Garage() {
    }


    public void addVehicle(Vehicle vehicle) {
//        if (isExist(vehicle)) { return; }
        if (vehicles.length == numOfVehicles) {
            vehicles = Arrays.copyOf(vehicles, vehicles.length * 2);
        }
        vehicles[numOfVehicles++] = vehicle;
    }

    private boolean isExist(Vehicle vehicle) {
        for (int i = 0; i < numOfVehicles; i++) {
            if (vehicle.equals(vehicles[i]));
            {
                return true;
            }
        }
        return false;
    }

    public void driveAll() {
        for (int i = 0; i < numOfVehicles; i++) {
            vehicles[i].drive();
        }
    }
}
