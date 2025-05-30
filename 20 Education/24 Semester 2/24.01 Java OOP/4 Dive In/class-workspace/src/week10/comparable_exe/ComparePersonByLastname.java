package week10.comparable_exe;

import java.util.Comparator;

public class ComparePersonByLastname implements Comparator<Person> {
    public int compare(Person p1, Person p2) {
        return p1.getLastname().compareTo(p2.getLastname());
    }
}
