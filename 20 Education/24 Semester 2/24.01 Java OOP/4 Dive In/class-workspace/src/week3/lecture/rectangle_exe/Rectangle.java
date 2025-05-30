package week3.lecture.rectangle_exe;

public class Rectangle {
    private int width = 10;
    private int height = 10;

    public Rectangle (){} // Empty Constructor

    public Rectangle (int width, int height){
        this.width = width;
        this.height = height;
    }

    public int getPerimeter(){
        return (width + height) * 2;
    }

    public int getArea(){
        return width * height;
    }

    public String showByChar (char ch){
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < height; i++){
            for (int j = 0; j < width; j++){
                sb.append(ch).append(" ");
            }
            sb.append('\n');
        }

        return sb.toString();
    }

    @Override
    public String toString() {
        return showByChar('*');
    }
}
