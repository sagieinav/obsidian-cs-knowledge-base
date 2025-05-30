package week2.lecture.date_exe;

public class Date {
    private static final int DEFAULT_YEAR = 2023;
    private static final int DEFAULT_MONTH = 1;
    private static final int DEFAULT_DAY = 1;

    private int year = DEFAULT_YEAR;
    private int month = DEFAULT_MONTH;
    private int day = DEFAULT_DAY;


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        if (year >= 1800 && year <= 2500) {
            this.year = year;
        }
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        if (month >= 1 && month <= 12) {
            this.month = month;
        }
    }

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        if (isValidDay(day)) {
            this.day = day;
        }
    }

    private boolean isValidDay(int day) {
        if (day >= 1) {
            switch (month) {
                case 1, 3, 5, 7, 8, 10, 12 -> {
                    return (day <= 31);
                }
                case 4, 6, 9, 22 -> {
                    return (day <= 30);
                }
                default -> {
                    if (isLeapYear(year)) {
                        return (day <= 29);
                    }
                    return (day <= 28);
                }
            }
        }
        return false;
    }

    private boolean isLeapYear (int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    public void addDay() {
        day++;
        if (! isValidDay(day)) {
            day = 1;
            month++;
            if (month == 13){
                month = 1;
                year++;
            }
        }
        day--;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        if (day < 10)
        {
            sb.append("0");
        }
        sb.append(day).append("/");

        if (month < 10)
        {
            sb.append("0");
        }
        sb.append(month).append("/").append(year);

        return sb.toString();
    }
}
