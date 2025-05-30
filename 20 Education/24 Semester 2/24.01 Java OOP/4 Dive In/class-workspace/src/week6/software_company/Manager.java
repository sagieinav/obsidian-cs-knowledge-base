package week6.software_company;

import static week6.software_company.CompanyStatus.*;

public class Manager extends Employee {
    private static final float RAISE_FACTOR = 1.15f;
    private static final int MAX_EMPLOYEES = 10;
    private  Employee[] employees;
    private int numOfEmployees;

    public Manager(String firstname, String lastname, float salary) {
        super(firstname, lastname, salary);
        employees = new Employee[MAX_EMPLOYEES];
    }

    public boolean addEmployee(Employee employee) {
        if (isExist(employee) || numOfEmployees == MAX_EMPLOYEES) {
            return false;
        }
        employees[numOfEmployees++] = employee;
        return true;
    }

    private boolean isExist(Employee employee) {
        for (int i = 0; i < numOfEmployees; i++){
            if (employees[i].equals(employee)){
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append("\n");
        if (numOfEmployees == 0) {
            return sb.append("\t").append("No employees yet\n").toString();
        }
        for (int i = 0; i < numOfEmployees; i++) {
            sb.append("\t").append(employees[i].getName()).append("\n");
        }
        return sb.toString();
    }

}