package week9.interface_exe;

import javax.swing.*;

public class GraphicUI implements Messageable {

    @Override
    public void showMessage(String message){
        JOptionPane.showMessageDialog(null, message);
    }

    @Override
    public String getString (String prompt){
        return JOptionPane.showInputDialog(prompt);
    }
}

