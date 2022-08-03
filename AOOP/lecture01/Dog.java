public class Dog {
	private int size;
	private String breed;
	private String name;
static String type = "mammal";

static String bark() {
return ("Ruff! Ruff");
}

	Dog(int dSize, String dBreed, String dName) {
		size = dSize;
		breed = dBreed;
		name = dName;
	}

public String toString(){
	return "This dog size  "+size+"\n type "+type+"\n Breed: "+ breed+ "\nName "+name+"\n Barking "+ bark();
}

	public int getSize() {
		return size;
	}

	public void setSize(int isize) {
		size = isize;
	}

	public String getBreed() {
		return breed;
	}

	public void setBreed(String abreed) {
		breed = abreed;
	}

	public String getName() {
		return name;
	}

	public void setName(String aname) {
		name = aname;
	}

}
