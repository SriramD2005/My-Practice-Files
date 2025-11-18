import java.awt.FlowLayout;

import javax.swing.*;
public class FlowLayoutCheck {
    public static void main(String arg[]){
        JFrame frame = new JFrame();
        frame.setLayout(new FlowLayout(FlowLayout.CENTER));
        JPanel panel = new JPanel();
        panel.add(new JButton("first"));
        panel.add(new JButton("second"));
        frame.add(panel);
        frame.setSize(500, 500);
        frame.setVisible(true);
    }
}
