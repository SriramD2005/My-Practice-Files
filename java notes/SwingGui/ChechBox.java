import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class ChechBox {
    static String onOrOff;
    public static void main(String args[]){
        JFrame frame = new JFrame();
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        JCheckBox check = new JCheckBox("Check Box");
        check.addItemListener(e -> {
            if (check.isSelected()) onOrOff = "On";
            else onOrOff = "Off";
            System.out.println(onOrOff);
        });
        frame.add(check);
        frame.setVisible(true);
    }
}
