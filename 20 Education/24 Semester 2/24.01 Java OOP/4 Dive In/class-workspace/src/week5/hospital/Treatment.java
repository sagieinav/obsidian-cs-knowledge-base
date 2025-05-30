package week5.hospital;

import java.time.LocalDate;

public class Treatment {
    private final String description;
    private final LocalDate date;
    private final Doctor performedBy;

    public Treatment(String description, LocalDate date, Doctor performedBy) {
        this.description = description;
        this.date = date;
        this.performedBy = performedBy;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return description + ", " + date + ", performed by: " + performedBy.getName();
    }
}
