package week7.shapes_exercise;

public class Square extends Shape{
    private int side;

    public Square(int frameThickness, COLORS color, int side) {
        super(frameThickness, color);
        this.side = side;
    }

//    public boolean equals(Object obj){
//        if (this == obj){
//            return true;
//        }
//        if (obj instanceof Square square){
//            return super.equals(square) && side == square.side;
//        }
//
//        return false;
//    }

    public boolean equals(Object obj){
        if (super.equals(obj)){
            return true;
        }

        if (obj instanceof Square square){
            return side == square.side;
        }

        return false;
    }

    @Override
    public double getArea(){
        return side * side;
    }

    @Override
    public double getPerimeter(){
        return side * 4;
    }
    
    public String printSquare(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < side; i++){
            sb.append(" ".repeat(side)).append("\n");
        }

        return sb.toString();
    }
}
