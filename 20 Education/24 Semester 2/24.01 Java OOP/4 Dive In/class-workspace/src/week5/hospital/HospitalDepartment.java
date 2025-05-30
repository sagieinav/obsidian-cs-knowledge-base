package week5.hospital;

import static week5.hospital.HospitalActionStatus.GENERAL_ERROR;

public class HospitalDepartment {
    private final String name;
    private final int roomCount;
    private Doctor[] doctors;
    private int numOfDoctors;
    private Patient[] patients;
    private int numOfPatients;

    public HospitalDepartment(String name, int roomCount) {
        this.name = name;
        this.roomCount = roomCount;
        this.doctors = new Doctor[0];
        this.patients = new Patient[0];
    }

    public HospitalActionStatus addDoctor(Doctor doctor) {
        // TODO Implement your code here
        return GENERAL_ERROR;
    }

    public HospitalActionStatus addPatient(Patient patient) {
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
