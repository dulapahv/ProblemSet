import java.util.ArrayList;

public class Arraylist {

	public static void main(String[] args) {
		// TODO code application logic here
		ArrayList club = new ArrayList();
		club.add("Spanky");
		club.add("Darla");
		club.add("BuckWheat");
		System.out.println(club);
		club.set(1, "Mikey");
		System.out.println(club);

		// object o1 = club.remove(2);
		// club.add(0,o1);
		club.add(0, club.remove(2));
		System.out.println(club);
	}

}
