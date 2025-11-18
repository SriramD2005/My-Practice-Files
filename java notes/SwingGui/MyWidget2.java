import javax.swing.*;
import java.awt.*;
import java.util.Random;
public class MyWidget2 {
    public static void main(String ars[]){
        JFrame frame = new JFrame();
        frame.setSize(300, 300);
        System.out.println(JFrame.EXIT_ON_CLOSE);// JFrame.EXIT_ON_CLOSE = 3(integer)
        frame.setDefaultCloseOperation(3);
        MyWid mw = new MyWid();
        frame.add(mw);
        frame.setVisible(true);
    }
}
class MyWid extends JPanel{
    public void paintComponent(Graphics g){
        g.fillRect(0, 0, this.getWidth(), this.getHeight());
        Random random = new Random();
        int red = random.nextInt(256);
        System.out.println(red);
        int green = random.nextInt(256);
        int blue = random.nextInt(256);
        Color color = new Color(red, green, blue);
        g.setColor(color);
        g.fillRect(this.getWidth()/2-50, this.getHeight()/2-50, 100, 100);
    }
}
