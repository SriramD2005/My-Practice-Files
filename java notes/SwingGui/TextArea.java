//If you add a Scroller to a TextArea you don't have to add the TextArea in the frame, as the Scroller wraps(contains)
//the TextArea with in itself, You gotta add Scroller only
import javax.swing.*;
import java.awt.*;
public class TextArea {
    public static void main(String args[]){
        JFrame frame = new JFrame();
        frame.setLayout(new FlowLayout());
        JTextArea tArea = new JTextArea(10,10);
        JScrollPane scroller = new JScrollPane(tArea);
        tArea.setLineWrap(true);
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        //frame.add(tArea);
        frame.add(scroller);
        frame.setSize(200,200);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
    }
}
