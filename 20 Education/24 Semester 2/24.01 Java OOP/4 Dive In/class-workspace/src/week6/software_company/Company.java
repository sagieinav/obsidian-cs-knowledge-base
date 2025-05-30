package week6.software_company;

public class Company {
    private final String name;
    private Employee[] employees;
    private int numOfEmployees;
    
    public Company(String name) {
        this.name = name;
        init();
    }

    public void init() {
        employees = new Employee[10];

        // Regular employees
        employees[numOfEmployees++] = new Employee("Mor", "Avner", 10000);
//        employees[numOfEmployees++] = new Employee("Tom", "Keren", 12000);

        // Developers
        Developer d1 = new Developer("Moshe", "Cohen", 20000);
        d1.addLang("Java");
        d1.addLang("Python");
        d1.addLang("c++");
        employees[numOfEmployees++] = d1;

        Developer d2 = new Developer("Liat", "Barak", 30000);
        d2.addLang("Java");
        d2.addLang("nodeJs");
        employees[numOfEmployees++] = d2;

        Developer d3 = new Developer("Kobi", "Shalom", 22000);
        d3.addLang("Python");
        d3.addLang("javascript");
        d3.addLang("dart");
        employees[numOfEmployees++] = d3;

        // Managers
        Manager m1 = new Manager("Galit", "Mor", 35000);
        m1.addEmployee(employees[0]);
        m1.addEmployee(employees[2]);
        employees[numOfEmployees++] = m1;

        Manager m2 = new Manager("Sharon", "David", 27000);
        m2.addEmployee(employees[1]);
        m2.addEmployee(employees[3]);
        m2.addEmployee(employees[4]);
        employees[numOfEmployees++] = m2;

    }

    public String runActions() {
        StringBuilder sb = new StringBuilder();
        sb.append("=== Company Actions ===\n");

//        for (int i = 0; i < numOfEmployees; i++) {
//            Employee e = employees[i];
//            sb.append(e).append("\n");
//
//            // Developer-specific action
//            if (e instanceof Developer d) {
//                sb.append("Trying to add Java language to Developer ").append(d.getName());
//                CompanyStatus success = d.addLang("Java");
//                sb.append(" :" ).append(success).append("\n");
//                sb.append("Trying to add Python language to Developer ").append(d.getName());
//                success = d.addLang("Python");
//                sb.append(" :" ).append(success).append("\n");
//            }
//
//            // Manager-specific action
//            if (e instanceof Manager m) {
//                sb.append("Trying to add employee: ")
//                        .append(employees[4].getName())
//                        .append(" to Manager: ").append(m.getName());
//                CompanyStatus success = m.addEmployee(employees[4]);
//                sb.append(" :" ).append(success).append("\n");
//                m.applyAllRaise();
//                m.applyRaise();
//                sb.append("manager ")
//                        .append(m.getName())
//                        .append(" after raise salary").append("\n");
//            }
//        }
//        Manager m = (Manager)employees[5];
//        sb.append("Trying to add employee: ")
//                .append(employees[4].getName())
//                .append(" to Manager: ").append(m.getName());
//        CompanyStatus success = m.addEmployee(employees[4]);
//        sb.append(" :" ).append(success).append("\n");
        sb.append("=== End of Company Actions ===\n");
        return sb.toString();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Company").append(name).append("\n");
        for (int i = 0; i < numOfEmployees; i++) {
            sb.append(employees[i]).append("\n");
        }
        return sb.toString();
    }
}
