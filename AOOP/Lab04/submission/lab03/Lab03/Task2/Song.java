public class Song {

	private String name;
	private String artist;
	private double playTime;

	public Song(String name, String artist, double playTime) {
		this.name = name;
		this.artist = artist;
		this.playTime = playTime;
	}

	public String toString() {

		return "song: " + name + ", artist: " + artist + ", playTime: " + playTime;
	}

	public double getPlayTime() {
		return playTime;
	}

	public String getArtist() {
		return artist;
	}

	public String getSongName() {
		return name;

	}
}