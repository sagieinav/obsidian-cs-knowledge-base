package week4.lecture.exe3;

public class Utils {
    public static String rjust (String st, int minWidth, char fillChar) {
        if (st.length() >= minWidth) {
            return st;
        }
//        return (fillChar + "").repeat(minWidth - st.length()) + st; // Lazy way
        return String.valueOf(fillChar).repeat(minWidth - st.length()) + st; // Best practice
    }
}
