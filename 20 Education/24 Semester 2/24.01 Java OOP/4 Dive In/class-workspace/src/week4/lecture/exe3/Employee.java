package week4.lecture.exe3;

public class Employee {
    private String name;
    private String department;
    private int id;
    private static int ID = 1000;

    public Employee(String name, String department) {
        setId();
        setName(name);
        setDepartment(department);
    }

    public void setName(String name) {
        this.name = Utils.rjust(name, 2, '_');
        this.name = this.name.substring(0, 2).toUpperCase();
    }

    public void setDepartment(String department) {
        this.department = Utils.rjust(department, 3, '_');
        this.department = this.department.substring(this.department.length() - 3).toLowerCase();
    }

    public void setId() {
        this.id = ++ID;
    }

    public String getName() {
        return this.name;
    }

    public String getDepartment() {
        return this.department;
    }

    public int getId() {
        return this.id;
    }

    @Override
    public String toString() {
        return getName() + getDepartment() + getId();
    }
}
