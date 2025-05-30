package week9.pizza_exe.classes;

import week9.pizza_exe.interfaces.PreparePizzable;

public class RegularPizza implements PreparePizzable {

    public void makeDough() {
        System.out.println("Preparing dough of Eshel");
    }

    public void makeSouce() {
        System.out.println("Putting OSEM sauce");
    }

    public void putCheese() {
        System.out.println("Putting flakes of yellow cheese");
    }
}
