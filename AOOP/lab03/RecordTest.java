public class RecordTest {
	public static void main(String[] args) {
		// Record id = new Record();
		// id.num = 2;
		// id.name = "Barney";
		Record id = createRecord(2, "Barney");
		System.out.println(id);

		tryobject(id);
		System.out.println(id);
	}

	public static void tryobject(Record r) {
		r.num = 100;
		r.name = "Fred";
	}

	public static Record createRecord(int num, String name) {
		Record t = new Record();
		t.num = num;
		t.name = "Barney";

	}

}
