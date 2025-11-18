import javax.swing.*;
import java.awt.*;
class TextFeild{
    public static void main(String args[]){
        JFrame frame = new JFrame();
        frame.setLayout(new FlowLayout());
        frame.setBackground(Color.DARK_GRAY);
        JTextField text = new JTextField(20);
        frame.add(text);
        frame.setSize(300,300);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        JButton button = new JButton("button");
        frame.add(button);
        button.addActionListener((e)->{
            if ("sri".equals(text.getText()))
            text.setText("done");
            text.selectAll();
        });
    }
}