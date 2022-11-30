import javax.swing.*;

public class BasicJFrame {
    public static void main(String[] args) {
        JFrame jf = new JFrame("The Basic JFrame");
        jf.setSize(500, 250);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setVisible(true);
    }
}
