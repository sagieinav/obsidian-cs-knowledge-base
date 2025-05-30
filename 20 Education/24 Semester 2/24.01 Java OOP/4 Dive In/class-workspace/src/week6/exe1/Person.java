package week6.exe1;

public class Person {
    protected int id;
    protected String name;

    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
    public void haveFun() {
        System.out.println("wondering what to do!");
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + ":" + id + ", " + name;
    }
}