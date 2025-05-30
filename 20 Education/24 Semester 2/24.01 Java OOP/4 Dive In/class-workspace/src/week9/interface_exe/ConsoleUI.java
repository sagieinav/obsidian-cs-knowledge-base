package week9.interface_exe;

import java.util.Scanner;

public class ConsoleUI implements Messageable{
    public static Scanner s = new Scanner(System.in);

    @Override
    public void showMessage (String message){
        System.out.println(message);
    }

    @Override
    public String getString (String prompt){
        System.out.println(prompt);
        return s.nextLine();
    }
}
