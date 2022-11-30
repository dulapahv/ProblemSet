import javax.swing.*;  
import java.awt.event.*;  

class MyWindow {
    JFrame jf = new JFrame("MyWindow");
    JMenuBar jmb = new JMenuBar();
    JMenu jm = new JMenu("File");
    JMenuItem jmi = new JMenuItem("Print Something Cute");
    JPanel jp = new JPanel();
    JTextField jtf = new JTextField("Try the File Menu");

    class DoIt implements ActionListener {
        public void actionPerformed(ActionEvent ae) {
            System.out.println("Something Cute");
        }
    }

    MyWindow() {
        jf.setSize(500, 100);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setJMenuBar(jmb);
        jmb.add(jm);
        jm.add(jmi);

        jf.getContentPane().add(jp);
        jp.add(jtf);

        jmi.addActionListener(new DoIt());

        jf.setVisible(true);
    }
}

public class DoMyWindow {
    public static void main(String[] args) {
        new MyWindow();
    }
}
