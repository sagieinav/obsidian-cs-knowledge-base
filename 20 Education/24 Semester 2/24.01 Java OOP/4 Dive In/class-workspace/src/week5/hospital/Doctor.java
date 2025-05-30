package week5.hospital;

public class Doctor {
    private final String firstName;
    private final String lastName;
    private final String licenseNumber;
    private final int yearsOfExperience;

    public Doctor(String firstName, String lastName, String licenseNumber, int yearsOfExperience) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.licenseNumber = licenseNumber;
        this.yearsOfExperience = yearsOfExperience;
    }

    @Override
    public String toString() {
        return firstName + " " + lastName + ", " + licenseNumber + ", " + yearsOfExperience;
    }

    public String getName() {
        return firstName + " " + lastName;
    }
}
