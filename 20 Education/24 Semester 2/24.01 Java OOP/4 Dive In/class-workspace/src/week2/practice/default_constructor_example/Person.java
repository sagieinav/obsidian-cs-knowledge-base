package week2.practice.default_constructor_example;

public class Person {
    private String id;
    private String name;

    public Person(String id, String name) {
        setId(id);
        setName(name);
    }

    public Person() {
        this("123", "Unknown name");
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Person{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                '}';
    }
}
