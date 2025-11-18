package SwingGui;
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.util.Random;
public class ProblemUsingInnerClass {
    private static JButton button = new JButton("Change Color");
    private static JFrame frame = new JFrame();
    static JButton b2 = new JButton("button 2");
    public static void main(String args[]){
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        components mw = new components();
        JTextField textfield = new JTextField("Select Your Color",100);
        frame.add(BorderLayout.NORTH, textfield);
        frame.add(BorderLayout.CENTER, mw);
        JPanel topPanel = new JPanel();
        topPanel.add(button);
        topPanel.add(b2);
        frame.add(BorderLayout.SOUTH, topPanel);
        //USING THE NESTED CLASS
        ButtonListener bl = new ButtonListener();
        B2Listener b2l = new B2Listener();
        button.addActionListener(bl);
        b2.addActionListener(b2l); 
        frame.setVisible(true);
    }
    static class ButtonListener implements ActionListener{
        public void actionPerformed(ActionEvent e){
            frame.repaint();
        }
    }
    static class B2Listener implements ActionListener{
        public void actionPerformed(ActionEvent e){
            b2.setText("i do nothing");
        }
    }
}
class components extends JPanel{
    public void paintComponent(Graphics g){
        Graphics2D g2d = (Graphics2D) g;
        super.paintComponent(g);//when resize this prevents the leftover drawings and inconsistencies.
        Random r = new Random();
        int red = r.nextInt(256);
        int green = r.nextInt(256);
        int blue = r.nextInt(256);
        Color c1 = new Color(red, green, blue);
        GradientPaint gp = new GradientPaint(0, 0, c1, this.getWidth(), this.getHeight(), Color.yellow);
        g2d.fillRect(0, 0, this.getWidth(), this.getHeight());
        g2d.setPaint(gp);
        g2d.fillOval(this.getWidth()/2-50, this.getHeight()/2-50, 100, 100);
    }
}
