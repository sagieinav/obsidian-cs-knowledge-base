package week10.shapes_exe;

import week7.shapes_exercise.COLORS;

public abstract class Shape implements Cloneable{
    protected int frameThickness;
    protected COLORS color;
    protected Supplier supplier;

    public Shape(int frameThickness, COLORS color, Supplier supplier) {
        this.frameThickness = frameThickness;
        this.color = color;
        this.supplier = supplier;
    }
    public abstract double getArea();
    public abstract double getPerimeter();

    public void setColor(COLORS color) {
        this.color = color;
    }

    public Supplier getSupplier() {
        return supplier;
    }

    public void setSupplier(Supplier supplier) {
        this.supplier = supplier;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj){
            return true;
        }
        if (obj instanceof Shape shape){
            return color == shape.color && frameThickness == shape.frameThickness;
        }
        return false;
    }

    @Override
    protected Shape clone() throws CloneNotSupportedException {
        return (Shape)super.clone();
    }

    @Override
    public String toString() {
        return getClass().getSimpleName();
    }
}
