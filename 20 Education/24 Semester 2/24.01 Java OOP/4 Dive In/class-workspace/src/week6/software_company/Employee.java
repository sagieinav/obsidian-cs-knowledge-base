package week6.software_company;

public class Employee {
    private static int ID = 1;
    protected static float RAISE_FACTOR = 1.04f;
    protected String id;
    protected String firstname;
    protected String lastname;
    protected String email;
    protected float salary;

    public Employee(String firstname, String lastname, float salary) {
        this.id = "emp_" + ID++;
        this.firstname = firstname;
        this.lastname = lastname;
        this.email = firstname + "." + lastname + "@email.com";
        this.salary = salary;
    }

    public void applyRaise() {
        salary *= RAISE_FACTOR;
    }

    public String getName() {
        return firstname + " " + lastname;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + ": name= " +
                firstname +
                " " +
                lastname +
                ", email= " +
                email +
                ", salary= " +
                salary;
    }

}
