package week5.hospital;

import java.time.LocalDate;

import static week5.hospital.HospitalActionStatus.GENERAL_ERROR;

public class Hospital {
    private final String name;
    private HospitalDepartment[] departments;
    private int numOfDepartments;

    public Hospital(String name) {
        this.name = name;
        this.departments = new HospitalDepartment[0];
    }

    public String init(){
        StringBuilder sb = new StringBuilder();
        int roomCount = 20;
        HospitalDepartment cardiology = new HospitalDepartment("Cardiology", roomCount);

        Doctor drSmith = new Doctor("John", "Smith", "MED‑12345", 10);
        Doctor drLee   = new Doctor("Emily", "Lee",  "MED‑67890",  5);

        HospitalActionStatus res = cardiology.addDoctor(drSmith);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Doctor ").append(drSmith.getName()).append(", Error: ").append(res).append("\n");
        }
        res = cardiology.addDoctor(drLee);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Doctor ").append(drLee.getName()).append(", Error: ").append(res).append("\n");
        }
        res = cardiology.addDoctor(drLee);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Doctor ").append(drLee.getName()).append(", Error: ").append(res).append("\n");
        }

        Patient alice = new Patient("Alice Brown", "123456789");
        Patient bob   = new Patient("Bob Johnson", "987654321");

        res = cardiology.addPatient(alice);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Patient ").append(alice.getName()).append(", Error: ").append(res).append("\n");
        }

        res = cardiology.addPatient(bob);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Patient ").append(bob.getName()).append(", Error: ").append(res).append("\n");
        }

        res = cardiology.addPatient(bob);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Patient ").append(bob.getName()).append(", Error: ").append(res).append("\n");
        }

        Treatment t1 = new Treatment(
                "ECG (Electrocardiogram)",
                LocalDate.of(2025, 4, 21),
                drSmith);

        Treatment t2 = new Treatment(
                "Cardiac catheterization",
                LocalDate.of(2025, 4, 22),
                drLee);

        res = alice.addTreatment(t1);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Treatment ").append(t1.getDescription()).append(", Error: ").append(res).append("\n");
        }

        res = alice.addTreatment(t2);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Treatment ").append(t1.getDescription()).append(", Error: ").append(res).append("\n");
        }

        res = bob.addTreatment(t1);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Treatment ").append(t1.getDescription()).append(", Error: ").append(res).append("\n");
        }

        res = bob.addTreatment(t1);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Treatment ").append(t1.getDescription()).append(", Error: ").append(res).append("\n");
        }


        res = addDepartments(cardiology);
        if (!res.equals(HospitalActionStatus.SUCCESS)){
            sb.append("Failed to add Departments ").append(cardiology.getName()).append(", Error: ").append(res).append("\n");
        }
        return sb.toString().isEmpty() ? "Init Hospital succeed... :)" : sb.toString();
    }

    public HospitalActionStatus addDepartments(HospitalDepartment department) {
        // TODO Implement your code here
        return GENERAL_ERROR;
    }


    @Override
    public String toString() {
        // TODO Implement your code here
        return null;
    }
}
