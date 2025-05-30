package week7.shapes_exercise;

import java.util.Arrays;
import java.util.Random;

public class ManageShapes {
    private final String name;
    private Shape[] shapes;
    private int numOfShapes;

    public ManageShapes(String name) {
        this.name = name;
        shapes = new Shape[2];
    }

    public String init(int amount){
        StringBuilder sb = new StringBuilder();
        Random r = new Random();
        COLORS color;
        int size, colorsLen = COLORS.values().length;
        SHAPES_STATUS res;
        Shape shape;
        int i = 0;
        while (i < amount){
            color = COLORS.values()[r.nextInt(colorsLen)];
            size = 1 + r.nextInt(10);

            if (r.nextInt(6) > 2){
                res = add(new Square(size, color, 1 + r.nextInt(6)));
            }

            i++;
        }
        return sb.toString();
    }


    private SHAPES_STATUS add(Shape shape) {
        if (isExist(shape)){
            return SHAPES_STATUS.SHAPE_EXIST;
        }

        if (shapes.length == numOfShapes){
            shapes = Arrays.copyOf(shapes, numOfShapes * 2);
        }

        shapes[numOfShapes] = shape;
        return SHAPES_STATUS.SUCCESS;
    }


    private boolean isExist(Shape shape) {
        for (int i = 0; i < numOfShapes; i++){
            if (shape.equals(shapes[i])){
                return true;
            }
        }
        return false;
    }


    public String getAllPerimeters() {
        // TODO Implement your code here
        return null;
    }

    public String getAllAreas() {
        // TODO Implement your code here
        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("All shapes in ").append(name).append(" Shapes System");
        // TODO Implement your code here
        return sb.toString();
    }
}
