package week9.pizza_exe.classes;

import week9.pizza_exe.interfaces.PreparePizzable;

public class SimplePizza implements PreparePizzable {

    public void makeDough() {
        System.out.println("Taking pita");
    }

    public void makeSouce() {
        System.out.println("Putting ketchup");
    }

    public void putCheese() {
        System.out.println("Putting slices of yellow cheese");
    }
}