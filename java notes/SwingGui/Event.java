import javax.swing.*;
import java.awt.event.*;
public class Event implements ActionListener {
    static JButton button = new JButton("Click me");
    public static void main(String args[]){
        JFrame frame = new JFrame();
        frame.add(button);
        Event e = new Event();
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        button.addActionListener(e);
    }
    public void actionPerformed(ActionEvent e){
        button.setText("I've been clicked");
    }
}
