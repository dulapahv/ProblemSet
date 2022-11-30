import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Converter extends JFrame implements ActionListener {
    private JLabel prompt = new JLabel("Distance in miles: ");
    private JTextField input = new JTextField(6);
    private JTextArea display = new JTextArea(10, 20);
    private JButton convert = new JButton("Convert!");

    public Converter() {
        getContentPane().setLayout(new FlowLayout());
        getContentPane().add(prompt);
        getContentPane().add(input);
        getContentPane().add(convert);
        getContentPane().add(display);
        display.setLineWrap(true);
        display.setEditable(false);
        convert.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        double miles = Double.valueOf(input.getText()).doubleValue();
        double km = miles * 1.60934;
        display.append(miles + " miles equals " + km + " kilometers\n");
    }

    public static void main(String[] args) {
        Converter f = new Converter();
        f.setSize(400, 300);
        f.setVisible(true);

        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }
}
