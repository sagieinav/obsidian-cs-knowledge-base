package week9.pizza_exe.classes;

import week9.pizza_exe.interfaces.PreparePizzable;


public class FancyPizza implements PreparePizzable {

    public void makeDough() {
        System.out.println("Preparing yeast pastry");
    }

    public void makeSouce() {
        System.out.println("Preparing sauce of fresh tomatoes");
    }

    public void putCheese() {
        System.out.println("Putting a lot of Mozzarella");
    }
}
