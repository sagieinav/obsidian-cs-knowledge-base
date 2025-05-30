package week7.shapes_exercise;

public abstract class Shape {
    protected int frameThickness;
    protected COLORS color;

    public Shape(int frameThickness, COLORS color) {
        this.frameThickness = frameThickness;
        this.color = color;
    }

    public boolean equals(Object obj){
        if (this == obj){
            return true;
        }
        if (obj instanceof Shape shape){
            return color == shape.color && frameThickness == shape.frameThickness;
        }
        return false;
    }

    public abstract double getArea();
    public abstract double getPerimeter();
}
