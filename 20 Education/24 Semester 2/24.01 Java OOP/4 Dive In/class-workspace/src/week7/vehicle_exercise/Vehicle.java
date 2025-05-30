package week7.vehicle_exercise;

import week7.vehicle_exercise.vehicle_types.Car;
import week7.vehicle_exercise.vehicle_types.Motorcycle;
import week7.vehicle_exercise.vehicle_types.Truck;

public class Vehicle {
    protected String licenseNumber;
    protected int year;
    protected double maxSpeed;


    public Vehicle(String licenseNumber, int year, double maxSpeed) {
        this.licenseNumber = licenseNumber;
        this.year = year;
        this.maxSpeed = maxSpeed;
    }

    public String getLicenseNumber() {
        return licenseNumber;
    }

    public void drive() {
        String st = this.getClass().getSimpleName();

        if (this instanceof Car){
            st += " is driving smoothly on the road";
        }

        else if (this instanceof Motorcycle){
            st += " Motorcycle is speeding between cars";
        }

        else if (this instanceof Truck){
            st += " Truck is hauling heavy cargo";
        }

        else {
            System.out.println("Oops... need to implement");
            return;
        }

        System.out.println(st);
    }

    @Override
    public boolean equals(Object obj){
        if (obj == this){
            return true;
        }
        if (obj instanceof Vehicle v){
            return licenseNumber.equals(v.licenseNumber) && year == v.year && maxSpeed == v.maxSpeed;
        }
        return super.equals(obj);
    }
}
