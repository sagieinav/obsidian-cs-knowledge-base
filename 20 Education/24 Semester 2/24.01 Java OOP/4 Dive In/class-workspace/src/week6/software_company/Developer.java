package week6.software_company;

import static week6.software_company.CompanyStatus.*;

public class Developer extends Employee {
    private static final float RAISE_FACTOR = 1.1f;
    private static final int MAX_LANGS = 6;
    private String[] progLangs;
    private int numOfLangs;

    public Developer(String firstName, String lastName, float salary) {
        super(firstName, lastName, salary);
        progLangs = new String[MAX_LANGS];
    }

    public boolean addLang(String lang) {
        if (isExist(lang) || numOfLangs == MAX_LANGS) {
            return false;
        }
        progLangs[numOfLangs++] = lang;
        return true;
    }

    private boolean isExist(String lang) {
        for (int i = 0; i < numOfLangs; i++){
            if (progLangs[i].equals(lang)){
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append("\n\tProgramming languages:");
        sb.append("[");
        for (int i = 0; i < numOfLangs; i++) {
            sb.append(progLangs[i]);
            if (i < numOfLangs - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return  sb.toString();
    }


}
