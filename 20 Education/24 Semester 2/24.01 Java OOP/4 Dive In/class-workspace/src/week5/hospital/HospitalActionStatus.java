package week5.hospital;

public enum HospitalActionStatus {
    GENERAL_ERROR("General Error"),
    SUCCESS("Success"),
    DEPARTMENTS_EXIST("Departments already exist"),
    DEPARTMENTS_NOT_EXIST("Departments not exist"),
    DOCTOR_EXIST("Doctor already exist"),
    DOCTOR_NOT_EXIST("Doctor not exist"),
    PATIENT_EXIST("Patient already exist"),
    PATIENT_NOT_EXIST("Patient not exist"),
    TREATMENT_EXIST("Treatment already exist"),
    TREATMENT_NOT_EXIST("Treatment not exist");

    private final String description;

    HospitalActionStatus(String description) {
        this.description = description;
    }


    @Override
    public String toString() {
        return description;
    }
}
