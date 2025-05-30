package week7.shapes_exercise;

public enum SHAPES_STATUS {
    SUCCESS("Action success"), SHAPE_EXIST("Shape already exist");

    private final String description;
    SHAPES_STATUS(String s) {
        description = s;
    }

    @Override
    public String toString() {
        return description;
    }
}
