package SwingGui;
import javax.swing.*;
import java.awt.*;
public class FirstJframe {
    public static void main(String args[]){
        JFrame frame = new JFrame();
        JButton button = new JButton("button");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(button);
        frame.setSize(300,300);
        MyWidget mw = new MyWidget();
        frame.getContentPane().add(mw);
        frame.setVisible(true);
    }
}
class MyWidget extends JPanel{
    public void paintComponent(Graphics g){
        Image image = new ImageIcon("C:\\Users\\srira\\Pictures\\Screenshots\\Screenshot 2025-03-23 190324.png").getImage();
        g.drawImage(image, 3, 4, this);
    }
}