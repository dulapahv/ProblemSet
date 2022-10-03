import javax.swing.JOptionPane;
import java.util.Formatter;

public class TemperatureTryCatch {
	public static void main(String[] args) {
		String openingMessage = "Please enter the current temperature in degrees F:";
		String outputMessage = "", temperatureStr = "";
		int temperature = 0;
		try {
			// input
			temperatureStr = JOptionPane.showInputDialog(openingMessage);
			temperature = Integer.parseInt(temperatureStr);
			// processing
			if (temperature < 30)
				outputMessage += "It is very cold outside!";
			else if (temperature < 50)
				outputMessage += "It is warm outside.";
			else if (temperature < 70)
				outputMessage += "It is cool outside.";
			else if (temperature < 90)
				outputMessage += "It is warm outside.";
			else
				outputMessage += "It is HOT outside!";
			// output
			JOptionPane.showMessageDialog(null, outputMessage, "Weather Report", JOptionPane.PLAIN_MESSAGE);
		} catch (NumberFormatException e) {
			String errorMessage = String.format("'%s' is invalid.\nPlease enter only digits.", temperatureStr);
			JOptionPane.showMessageDialog(null, errorMessage);
			System.exit(0);
		}
		System.exit(0);
	} // end main method
} // end class
