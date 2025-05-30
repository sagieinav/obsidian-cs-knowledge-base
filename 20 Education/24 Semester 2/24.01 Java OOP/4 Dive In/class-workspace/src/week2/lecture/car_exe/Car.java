package week2.lecture.car_exe;

import week2.lecture.Util;

public class Car {
//    private String manufacturer;
//    private String model;
//    private int year;
//    private String color;
    private String carId;
    private int speed;

    public String getCarId() {
        return carId;
    }

    public void setCarId(String carId) {
        if (Util.validateCarNumber(carId)) {
            this.carId = carId;
        }
    }

    public int getSpeed() {
        return speed;
    }

    public void accelerate() {
        this.speed++;
    }

    public void decelerate() {
        this.speed--;
    }

    public void stop() {
        while (this.speed != 0) {
            this.speed--;
        }
    }

    public void getCarDetails(String carId, int speed)
    {
        System.out.println("Car ID: " + carId + "\nCar speed: " + speed);
    }

    @Override
    public String toString() {
        return "Car Number: " + carId + "\nSpeed: " + speed;
    }
}
