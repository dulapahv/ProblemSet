public class DogApp {
	public static void main(String[] args) {
		Dog d = new Dog(40, "Beagle", "Jill");
		System.out.println(d.toString());
		d.setSize(45);
		System.out.println(d.toString());
		Dog dp = new Dog(30, "Papillon", "Joe");
		System.out.println(dp.toString());
		dp.setSize(32);
		System.out.println(dp.toString());

		System.out.println("The first dog named " + d.getName() + "\nThe second dog named " + dp.getName());
	}
}
