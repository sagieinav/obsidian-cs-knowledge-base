package week10.shapes_exe;


import week7.shapes_exercise.COLORS;

public class Circle extends Shape {
    private double radius;
    public Circle(int frameThickness, COLORS color, double radius,Supplier supplier) {
        super(frameThickness, color, supplier);
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public double getPerimeter() {
        return Math.PI * radius * 2;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj){
            return true;
        }
        if (obj instanceof Circle circle){
            //Circle circle = (Circle) obj;
            return super.equals(circle) && radius == circle.radius;
        }
        return false;
    }

    @Override
    public String toString() {
        return super.toString() + " " + radius + ", " + color + ", " + supplier;
    }
}
