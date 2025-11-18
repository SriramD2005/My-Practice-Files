import javax.swing.*;
import java.awt.*;
public class G2D {
    public static void main(String ar[]){
    JFrame frame = new JFrame();
    frame.setSize(300, 300);
    frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
    JPanel mw = new My2DG();
    frame.add(mw);
    frame.setVisible(true);
}}
class My2DG extends JPanel{
    public void paintComponent(Graphics g){
        Graphics2D g2d = (Graphics2D) g;
        //GradientPaint class is used to make a combination of colors in the graphics object
        GradientPaint gp = new GradientPaint(70, 70, Color.blue, 150, 150, Color.red);
        g2d.setPaint(new GradientPaint(0, 0, Color.black, this.getWidth(), this.getHeight(), Color.yellow));
        g2d.fillRect(0, 0, this.getWidth(), this.getHeight());
        g2d.setPaint(gp);
        g2d.fillOval(70, 70, 100, 100);
    }
}