package week9.pizza_exe;

import week9.pizza_exe.classes.FancyPizza;
import week9.pizza_exe.classes.RegularPizza;
import week9.pizza_exe.classes.SimplePizza;
import week9.pizza_exe.interfaces.MakeDoughable;
import week9.pizza_exe.interfaces.MakeSouceable;
import week9.pizza_exe.interfaces.PreparePizzable;
import week9.pizza_exe.interfaces.PutCheeseable;

public class Main {

	public static void main(String[] args) {
		run1();
		System.out.println();
		run2();
	}
	private static void run1() {
		System.out.println("Preparing regular pizza:");
		preparePizza(new RegularPizza());
		System.out.println();

		System.out.println("Preparing simple pizza:");
		preparePizza(new SimplePizza());
		System.out.println();

		System.out.println("Preparing fancy pizza:");
		preparePizza(new FancyPizza());
	}


	private static void preparePizza(PreparePizzable p) {
		p.makeDough();
		p.makeSouce();
		p.putCheese();
	}

	private static void run2() {
		PreparePizzable[] pizzaMakers = new PreparePizzable[3];
		pizzaMakers[0] = new RegularPizza();
		pizzaMakers[1] = new SimplePizza();
		pizzaMakers[2] = new FancyPizza();
		int counter = 1;
        for (PreparePizzable pizzaMaker : pizzaMakers) {
            for (PreparePizzable maker : pizzaMakers) {
                for (PreparePizzable preparePizzable : pizzaMakers) {
                    System.out.println("Pizza #" + counter);
                    preparePizza(pizzaMaker, maker, preparePizzable);
                    counter++;
                    System.out.println();
                }
            }
        }
	}
	private static void preparePizza(MakeDoughable dough, MakeSouceable souce, PutCheeseable cheese) {
		dough.makeDough();
		souce.makeSouce();
		cheese.putCheese();
	}
	/*
	Pizza #1
	Prepare dough of Eshel
	Put OSEM souce
	Put flakes of yellow cheese

	Pizza #2
	Prepare dough of Eshel
	Put OSEM souce
	Put slice of yellow cheese

	Pizza #3
	Prepare dough of Eshel
	Put OSEM souce
	Put a lot of Muzarella

	Pizza #4
	Prepare dough of Eshel
	Put ketcup
	Put flakes of yellow cheese

	Pizza #5
	Prepare dough of Eshel
	Put ketcup
	Put slice of yellow cheese

	Pizza #6
	Prepare dough of Eshel
	Put ketcup
	Put a lot of Muzarella

	Pizza #7
	Prepare dough of Eshel
	Prepare souce of fresh tomatoes
	Put flakes of yellow cheese

	Pizza #8
	Prepare dough of Eshel
	Prepare souce of fresh tomatoes
	Put slice of yellow cheese

	Pizza #9
	Prepare dough of Eshel
	Prepare souce of fresh tomatoes
	Put a lot of Muzarella

	Pizza #10
	Take pitta
	Put OSEM souce
	Put flakes of yellow cheese

	Pizza #11
	Take pitta
	Put OSEM souce
	Put slice of yellow cheese

	Pizza #12
	Take pitta
	Put OSEM souce
	Put a lot of Muzarella

	Pizza #13
	Take pitta
	Put ketcup
	Put flakes of yellow cheese

	Pizza #14
	Take pitta
	Put ketcup
	Put slice of yellow cheese

	Pizza #15
	Take pitta
	Put ketcup
	Put a lot of Muzarella

	Pizza #16
	Take pitta
	Prepare souce of fresh tomatoes
	Put flakes of yellow cheese

	Pizza #17
	Take pitta
	Prepare souce of fresh tomatoes
	Put slice of yellow cheese

	Pizza #18
	Take pitta
	Prepare souce of fresh tomatoes
	Put a lot of Muzarella

	Pizza #19
	Prepare yeast pastry
	Put OSEM souce
	Put flakes of yellow cheese

	Pizza #20
	Prepare yeast pastry
	Put OSEM souce
	Put slice of yellow cheese

	Pizza #21
	Prepare yeast pastry
	Put OSEM souce
	Put a lot of Muzarella

	Pizza #22
	Prepare yeast pastry
	Put ketcup
	Put flakes of yellow cheese

	Pizza #23
	Prepare yeast pastry
	Put ketcup
	Put slice of yellow cheese

	Pizza #24
	Prepare yeast pastry
	Put ketcup
	Put a lot of Muzarella

	Pizza #25
	Prepare yeast pastry
	Prepare souce of fresh tomatoes
	Put flakes of yellow cheese

	Pizza #26
	Prepare yeast pastry
	Prepare souce of fresh tomatoes
	Put slice of yellow cheese

	Pizza #27
	Prepare yeast pastry
	Prepare souce of fresh tomatoes
	Put a lot of Muzarella
	*/

}

