import javax.swing.*;
import java.awt.*;
public class FlowLayoutPractice {
    public static void main(String arg[]){
        JFrame frame = new JFrame();
        JPanel panel = new JPanel();
        panel.setBackground(Color.DARK_GRAY);
        JButton b1 = new JButton("button 1");
        JButton b2 = new JButton("small");
        JButton b3 = new JButton("a big button");
        frame.add(BorderLayout.EAST, panel);
        panel.add(b1);
        panel.add(b3);
        panel.add(b2);
        JButton b4 = new JButton("small");
        panel.add(b4);
        frame.setSize(300,300);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
    }
}

