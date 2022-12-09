import javax.swing.JOptionPane;

public class PasswordGuiApp {
	public static void main(String[] args) {
		while (true) {
			String passwd = JOptionPane.showInputDialog("Enter a password");
			if (PasswordVerifier.isValid(passwd)) {
				JOptionPane.showMessageDialog(null, "Valid password.");
				break;
			} else {
				JOptionPane.showMessageDialog(null, "Invalid password.");
			}
		}
	}
}
