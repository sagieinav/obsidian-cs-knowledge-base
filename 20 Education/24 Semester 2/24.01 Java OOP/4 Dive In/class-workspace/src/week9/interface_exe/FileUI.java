package week9.interface_exe;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class FileUI implements Messageable{
    public Scanner s;
    private final String filePath;

    public FileUI() {
        String packagePath = getClass().getPackage().getName().replace('.', File.separatorChar);
        filePath = System.getProperty("user.dir")
                + File.separator + "3 Workspace"
                + File.separator + "src"
                + File.separator + packagePath + File.separator;
        System.out.println(filePath);
    }

    @Override
    public void showMessage(String message) {
        File f = new File(filePath + File.separator + "output.txt");
        PrintWriter pw = null;
        try {
            pw = new PrintWriter(f);
            pw.println(message);
        }

        catch(FileNotFoundException e) {
            System.out.println(e.getMessage());
        }

        finally {
            if (pw != null){
                pw.close();
            }
        }

    }

    @Override
    public String getString(String prompt) {
        File f = new File(filePath + File.separator + "output.txt");
        String fileName = null;

        try{
            s = new Scanner(f);
            fileName = s.nextLine();
        }

        catch(FileNotFoundException e){
            System.out.println(e.getMessage());
        }

        finally {
            if (s != null){
                s.close();
            }
        }

        return fileName;
    }
}
