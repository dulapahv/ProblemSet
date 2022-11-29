import java.io.IOException;
import java.net.*;

public class TestSocket {
    public static void main(String[] args) {
        String host = "localhost";
        for (int i = 100; i < 200; i++) {
            try {
                Socket s = new Socket(host, i);
                System.out.println("There is a server on port :" + i + "  of:  " + host);
            } catch (UnknownHostException e) {
                System.err.println(e);
            } catch (IOException ie) {
                System.out.println(ie.getMessage());
            }
        }
    }
}