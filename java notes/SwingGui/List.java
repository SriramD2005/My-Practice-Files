// the JList is created only to show the data, you cannot add live components
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class List {
    public static void main (String args[]){
        JFrame frame = new JFrame();
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        //JButton[] buttonList = {new JButton("button 1"), new JButton("button 2"), new JButton("button 3"), new JButton("button 4"), new JButton()};
        //JList List = new JList<JButton>(buttonList);
        //The above lines of code will not work as expected
        String[] flist = {"Sriram", "Sreenithi", "Dayalan", "Kavitha"};
        JList List = new JList(flist);
        JScrollPane scroller = new JScrollPane(List);
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        frame.add(scroller);
        frame.setVisible(true);
    }
}
