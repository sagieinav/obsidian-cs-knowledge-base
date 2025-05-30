package week2.lecture.person_array_exe;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person();
        p1.setName("Sagi");
        p1.setHeight(174);
        p1.setWeight(300.2f);

        Person p2 = new Person();
        p2.setName("Avi");
        p2.setHeight(150);
        p2.setWeight(84.5f);

        Person p3 = new Person();
        p3.setName("Moshe");
        p3.setHeight(190);
        p3.setWeight(55.2f);

        Person[] persons = {p1, p2, p3};
        System.out.println(Arrays.toString(persons)); // Print the persons array

        Person[] personsByWeight = sortByWeight(persons);
        System.out.println(Arrays.toString(personsByWeight));
    }

    private static Person[] sortByWeight(Person[] persons)
    {
        Person[] personsByWeight = Arrays.copyOf(persons, persons.length);
        bubbleSort(personsByWeight);
        return personsByWeight;
    }

    private static void bubbleSort(Person[] arr)
    {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j].getWeight() > arr[j + 1].getWeight()) {

                    // swap temp and arr[i]
                    Person temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }
}
