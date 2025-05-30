package week9.interface_exe;

public class Main {
    public static void main(String[] args) {
//        {
//            ConsoleUI consoleUI = new ConsoleUI();
//            String name = consoleUI.getString("What is your name?");
//            consoleUI.showMessage("Hi " + name);
//            ConsoleUI.s.close();
//        }
//
//        {
//            GraphicUI graphicUI = new GraphicUI();
//            String name = graphicUI.getString("What is your name?");
//            graphicUI.showMessage("Hi " + name);
//        }

        {
            FileUI fileUI = new FileUI();
            String name = fileUI.getString("What is your name?");
            fileUI.showMessage("Hi " + name);
        }

        }
    }
