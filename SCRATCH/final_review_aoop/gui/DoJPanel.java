import javax.swing.*;

public class DoJPanel {
    public static void main(String[] agrs) {
        JFrame jf = new JFrame("The Basic JFrame");
        jf.setSize(500, 250);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel jp = new JPanel();
        jf.getContentPane().add(jp);

        jf.setVisible(true);
    }
}
