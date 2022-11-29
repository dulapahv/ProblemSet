import java.io.*;
import java.net.*;
import javax.swing.*;

public class DateClient {
    public static void main(String[] args) throws IOException {
        InetAddress x = InetAddress.getLocalHost();
        System.out.println(x);
        Socket s = new Socket(x, 9090);
        BufferedReader input = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String answer = input.readLine();
        JOptionPane.showMessageDialog(null, answer);
        System.exit(0);
    }

}
