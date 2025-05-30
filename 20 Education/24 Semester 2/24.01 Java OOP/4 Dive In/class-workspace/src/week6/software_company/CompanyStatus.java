package week6.software_company;

public enum CompanyStatus {
    LANGUAGE_NO_ROOM("There is not enough space to add a language to the array."),
    LANGUAGE_ALREADY_EXIST("Language already exists."),
    EMPLOYEES_NO_ROOM("There is not enough space to add an employee to the array."),
    EMPLOYEE_ALREADY_EXIST("Employee already exist."),
    SUCCESS("Action success");

    private final String description;

    CompanyStatus(String description) {
        this.description = description;
    }

    @Override
    public String toString() {
        return description;
    }
}
