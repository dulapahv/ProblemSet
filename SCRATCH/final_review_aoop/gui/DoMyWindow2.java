import javax.swing.*;
import java.awt.event.*;

public class DoMyWindow2 {
    public static void main(String[] args) {
        new MyWindow2();
    }
}

class MyWindow2 extends JFrame {
    JMenuBar jmb = new JMenuBar();
    JMenu jm = new JMenu("File");
    JMenuItem jmi = new JMenuItem("Print Something Cute");
    JPanel jp = new JPanel();
    JTextField jtf = new JTextField("Try the File Menu");
    int count = 0;

    class DoIt implements ActionListener {
        public void actionPerformed(ActionEvent ae) {
            System.out.println("Something Cute");
            jtf.setText("Count = " + ++count);
        }
    }

    MyWindow2() {
        setSize(500, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setJMenuBar(jmb);
        jmb.add(jm);
        jm.add(jmi);
        jmi.addActionListener(new DoIt());
        getContentPane().add(jp);
        jp.add(jtf);
        setVisible(true);
    }
}
