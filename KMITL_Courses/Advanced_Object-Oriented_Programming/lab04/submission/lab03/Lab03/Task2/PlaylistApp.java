public class PlaylistApp {

	public static void main(String[] args) {

		Song s1 = new Song("Yellow", "Cold Play", 2.4);
		Song s2 = new Song("Clocks", "Cold Play", 3.56);
		Song s3 = new Song("Around the Sun", "REM", 4.30);
		Playlist p = new Playlist("ColdPlayHits");
		if (!p.isSongInPlaylist(s1.getSongName())) {
			p.addSong(s1);
		}
		if (!p.isSongInPlaylist(s2.getSongName())) {
			p.addSong(s2);
		}
		if (!p.isSongInPlaylist(s3.getSongName())) {
			p.addSong(s3);
		}
		System.out.println("Playlist: " + p.playlistName());
		System.out.println("\tNumber of songs in playlist is " + p.totalSongs());
		System.out.println("\tTotal playtime of playlist is " + p.playlistTime());
		if (p.isSongInPlaylist(s2.getSongName())) {
			p.removeSong(s2);
		}

		if (!p.isSongInPlaylist(s2.getSongName())) {
			p.addSong(s2);
		}
		if (!p.isSongInPlaylist(s3.getSongName())) {
			p.addSong(s3);
		}

		System.out.println("\nUpdateed playlist: " + p.playlistName());
		System.out.println("\tNumber of songs in playlist " + p.playlistName() + " is " + p.totalSongs());
		System.out.println("\tTotal playtime of playlist " + p.playlistName() + " is " + p.playlistTime());

		// System.out.println(p.isSongInPlaylist("Clocks"));
		System.out.println("\nSongs by Cold Play in playlist :" + p.playlistName());
		p.songsByArtist("Cold Play");

		System.out.println("\nSongs by Jeff Beck in playlist :" + p.playlistName());
		p.songsByArtist("Jeff Beck");

		System.out.println("\nAll songs in the playlist: " + p.playlistName() + " ");
		for (Song s : p.getList()) {
			System.out.println(
					"\tSong: " + s.getSongName() + " Artist: " + s.getArtist() + " Pplay time: " + s.getPlayTime());
		}

		Playlist v = new Playlist("HotPlayHits");
		Song s4 = new Song("Grease Monkey", "Jeff Beck", 4.30);
		v.addSong(s4);
		v.addSong(s3);
		System.out.println("\nPlaylist: " + v.playlistName());
		System.out.println("\tNumber of songs in playlist is " + v.totalSongs());
		System.out.println("\tTotal playtime of playlist is " + v.playlistTime());

		System.out.println("\nAll songs in the playlist: " + v.playlistName() + " ");
		for (Song s : v.getList()) {
			System.out.println(
					"\tSong: " + s.getSongName() + " Artist: " + s.getArtist() + " Pplay time: " + s.getPlayTime());
		}

		v.addSongsFrom(p);

		System.out.println("\nUpdated Playlist: " + v.playlistName());
		System.out.println("\tNumber of songs in playlist is " + v.totalSongs());
		System.out.println("\tTotal playtime of playlist is " + v.playlistTime());

		System.out.println("\nAll songs in the playlist: " + v.playlistName() + " ");
		for (Song s : v.getList()) {
			System.out.println(
					"\tSong: " + s.getSongName() + " Artist: " + s.getArtist() + " Pplay time: " + s.getPlayTime());
		}
	}

}
