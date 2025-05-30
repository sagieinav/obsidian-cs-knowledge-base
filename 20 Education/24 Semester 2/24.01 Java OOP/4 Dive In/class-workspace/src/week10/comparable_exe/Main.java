package week10.comparable_exe;

import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws CloneNotSupportedException {
		Person[] persons = new Person[8];
		persons[0] = new Student("224728850", "Or", "Rosen", 23, 95.2);
		persons[1] = new Student("983515150", "Shlomi", "Levy", 30, 95.2);
		persons[2] = new Lecturer("969136386", "Tal", "Lapidot", 45, 7);
		persons[3] = new Student("150604087", "Yael", "Aviv", 22, 95.2);
		persons[4] = new Student("406710980", "Elad", "Ohana", 28, 95.2);
		persons[5] = new Student("540663071", "Gilad", "Avitan", 27, 95.2);
		persons[6] = new Lecturer("348026231", "Gali", "Golan", 37, 4);
		persons[7] = new Student("154160635", "Hadar", "Levin", 25, 95.2);

		System.out.println("A: Sort Students by age");
		try{
			sortPersonByAge(persons);
		}catch (Exception e){
			System.out.println("Error in A: " + e.getMessage());
		}

		System.out.println("B: Sort Students by firstname and after that by lastname");
		try{
			sortByNamePerson2Array(persons);
		}catch (Exception e){
			System.out.println("Error in B: " + e.getMessage());
		}

		System.out.println("C: clone elements");
		try{
			copyArrayWithClone(persons);
		}catch (Exception e){
			System.out.println("Error in C: " + e.getMessage());
		}
	}

	private static void sortPersonByAge(Person[] persons) {
		System.out.println("before sorting by age");
		print(persons);
		Arrays.sort(persons);
		System.out.println("\nafter  sorting by age");
		print(persons);
	}

	private static void sortByNamePerson2Array(Person[] persons) {
		System.out.println("before sorting");
		print(persons);

		Arrays.sort(persons, new ComparePersonByFirstname());

		System.out.println("\nafter  sorting by firstname");
		print(persons);
		// TODO implement your code
		System.out.println("\nafter  sorting by lastname");
		print(persons);
	}


	private static void copyArrayWithClone(Person[] persons) throws CloneNotSupportedException {
		Person[] newPersons = new Person[persons.length];
		// TODO implement your code
		System.out.println("before change in original array");
		System.out.println(persons[0]);
		System.out.println(newPersons[0]);
		persons[0].setAge(20);
		System.out.println("after change in original array");
		System.out.println(persons[0]);
		System.out.println(newPersons[0]);
	}

	private static void print(Person[] persons) {
        for (Person person : persons) {
            System.out.println(person);
        }
	}

}
