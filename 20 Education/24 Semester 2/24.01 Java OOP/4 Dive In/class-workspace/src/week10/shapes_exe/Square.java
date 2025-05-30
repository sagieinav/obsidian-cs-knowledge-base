package week10.shapes_exe;

import week7.shapes_exercise.COLORS;

public class Square extends Shape {
    private final int side;

    public Square(int frameThickness, COLORS color, int side, Supplier supplier) {
        super(frameThickness, color, supplier);
        this.side = side;
    }

    @Override
    public double getArea() {
        return side * side;
    }

    @Override
    public double getPerimeter() {
        return 4 * side;
    }

    public String show(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < side; i++) {
            sb.append("* ".repeat(side)).append("\n");
        }
        return sb.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj){
            return true;
        }
        if (obj instanceof Square square){
            return super.equals(square) && side == square.side;
        }
        return false;
    }

    @Override
    public String toString() {
        return super.toString() + " " + side + ", " + color + ", " + supplier;
    }
}
