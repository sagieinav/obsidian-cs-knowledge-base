package week5.hospital;

import static week5.hospital.HospitalActionStatus.GENERAL_ERROR;

public class Patient {
    private final String name;
    private final String idNumber;
    private Treatment[] treatments;
    private int numOfTreatments;

    public Patient(String name, String idNumber) {
        this.name = name;
        this.idNumber = idNumber;
        this.treatments = new Treatment[0];
    }

    public HospitalActionStatus addTreatment(Treatment treatment) {
        // TODO Implement your code here
        return GENERAL_ERROR;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        // TODO Implement your code here
        return null;
    }

}
