package week7.shapes_exercise;

public class Circle extends Shape{
    private double radius;
    public Circle(int frameThickness, COLORS color, double radius){
        super(frameThickness, color);
        this.radius = radius;
    }

    public boolean equals(Object obj){
        if (this == obj){
            return true;
        }
        if (obj instanceof Circle circle){
            return super.equals(circle) && radius == circle.radius;
        }

        return false;
    }

    @Override
    public double getArea(){
        return (Math.PI * radius * radius);
    }

    @Override
    public double getPerimeter(){
        return (Math.PI * radius * 2);
    }
}
