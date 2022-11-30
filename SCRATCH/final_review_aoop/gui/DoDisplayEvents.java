import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class DisplayEvents extends JFrame {
    JPanel jp = new JPanel(new BorderLayout());
    JTextArea ta = new JTextArea();
    JScrollPane jsp = new JScrollPane(ta);
    JButton jb = new JButton("The Button");

    DisplayEvents() {
        setSize(600, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().add(jp);
        ta.setFont(new Font("SansSerif", Font.PLAIN, 18));
        jb.setFont(new Font("SansSerif", Font.PLAIN, 18));
        jp.add(jsp, BorderLayout.CENTER);
        jp.add(jb, BorderLayout.SOUTH);
        jb.setBackground(Color.yellow);

        jb.addMouseListener(new ML());
        jb.addFocusListener(new FL());
        jb.addKeyListener(new KL());
        jb.addMouseMotionListener(new MML());

        setVisible(true);
    }

    class ML implements MouseListener {
        public void mouseClicked(MouseEvent e) {
            ta.append("mouseClicked - " + e.paramString() + "\n");
        }

        public void mouseEntered(MouseEvent e) {
            ta.append("mouseEntered - " + e.paramString() + "\n");
        }

        public void mouseExited(MouseEvent e) {
            ta.append("mouseExited - " + e.paramString() + "\n");
        }

        public void mousePressed(MouseEvent e) {
            ta.append("mousePressed - " + e.paramString() + "\n");
        }

        public void mouseReleased(MouseEvent e) {
            ta.append("mouseReleased - " + e.paramString() + "\n");
        }
    }

    class FL implements FocusListener {
        public void focusGained(FocusEvent e) {
            ta.append("focusGained - " + e.paramString() + "\n");
        }

        public void focusLost(FocusEvent e) {
            ta.append("focusLost - " + e.paramString() + "\n");
        }
    }

    class KL implements KeyListener {
        public void keyPressed(KeyEvent e) {
            ta.append("keyPressed - " + e.paramString() + "\n");
        }

        public void keyReleased(KeyEvent e) {
            ta.append("keyReleased - " + e.paramString() + "\n");
        }

        public void keyTyped(KeyEvent e) {
            ta.append("keyTyped - " + e.paramString() + "\n");
        }
    }

    class MML implements MouseMotionListener {
        public void mouseDragged(MouseEvent e) {
            ta.append("mouseDragged - " + e.paramString() + "\n");
        }

        public void mouseMoved(MouseEvent e) {
            ta.append("mouseMoved - " + e.paramString() + "\n");
        }
    }

}

public class DoDisplayEvents {
    public static void main(String[] args) {
        new DisplayEvents();
    }
}
