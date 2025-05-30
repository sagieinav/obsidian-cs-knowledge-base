package week7.shapes_exercise;

public class Main {
    public static void main(String[] args) {
        ManageShapes manageShapes = new ManageShapes("OOP Course");
        System.out.println();
        String res = manageShapes.init(6);
        if (res.isEmpty()){
            System.out.println("Init success without errors...:)");
        } else{
            System.out.println(res);
        }
        System.out.println(manageShapes);
        System.out.println(manageShapes.getAllAreas());
        System.out.println(manageShapes.getAllPerimeters());
    }
}


