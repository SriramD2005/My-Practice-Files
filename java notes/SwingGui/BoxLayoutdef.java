import javax.swing.*;
import java.awt.*;
//ByDefault:
//Flow Layout - Panel
//Box Layout - None
//Border Layout - Frame
public class BoxLayoutdef {
    public static void main(String args[]){
        JFrame frame = new JFrame();
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, 1));
        panel.setBackground(Color.DARK_GRAY);
        JButton b1 = new JButton("First button");
        JButton b2 = new JButton("Second");
        JButton b3 = new JButton("third");
        panel.add(b1);
        panel.add(b2);
        panel.add(b3);
        frame.add(BorderLayout.EAST, panel);
        System.out.println(BorderLayout.EAST);
        frame.setSize(400,400);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        
    }
}
