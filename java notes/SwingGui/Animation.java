import javax.swing.*;
import java.awt.*;
import java.util.concurrent.TimeUnit;
public class Animation {
    static double x, y;
    public static void main(String args[]){
        x = 0;
        y = 0;
        JFrame frame = new JFrame();
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        ball b = new ball();
        frame.getContentPane().add(b);
        double m = (double)frame.getContentPane().getHeight()/frame.getContentPane().getWidth();
        System.out.println(frame.getContentPane().getSize());
        frame.setVisible(true);
        while (x<frame.getWidth()){
            y = m*x;
            //System.out.println(y);
            try{
            TimeUnit.MILLISECONDS.sleep(50);
            }
            catch(Exception e){
                System.out.println(e.getMessage());
            }
            frame.repaint();
            x++;
        }
    }
    static class ball extends JPanel{
        public void paintComponent(Graphics g){
            super.paintComponent(g);
            g.fillRect(0, 0, this.getWidth(), this.getHeight());
            g.setColor(Color.red);
            g.fillOval((int)x, (int)y, 20, 20);
        }
    }
}
