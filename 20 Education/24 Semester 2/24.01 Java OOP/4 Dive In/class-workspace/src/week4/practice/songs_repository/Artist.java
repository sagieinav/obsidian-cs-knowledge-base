package week4.practice.songs_repository;

import java.util.Arrays;

public class Artist {

    private String name;
    private Song[] writtenSongs;
    private Song[] performedSongs;

    public Artist(String name) {
        this.name = name;
        writtenSongs = new Song[0];
        performedSongs = new Song[0];
    }

    public String getName() {
        return this.name;
    }

    public boolean hasWroteSong(Song theSong){
        for (Song s : writtenSongs) {
            if (s.equals(theSong)){
                return true;
            }
        }
        return false;
    }

    public boolean addWrittenSong(Song newSong){
        if (hasWroteSong(newSong)) {
            return false;
        }
        writtenSongs = Arrays.copyOf(writtenSongs, writtenSongs.length + 1);
        writtenSongs[writtenSongs.length - 1] = newSong;
        return true;
    }

    public boolean hasPerformedSong(Song theSong){
        for (Song s : performedSongs) {
            if (s.equals(theSong)){
                return true;
            }
        }
        return false;
    }

    public boolean addPerformedSong (Song newSong){
        if (hasPerformedSong(newSong)) {
            return false;
        }
        performedSongs = Arrays.copyOf(performedSongs, performedSongs.length + 1);
        performedSongs[performedSongs.length - 1] = newSong;
        return true;
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append(", Written songs: \n");
        for (Song s : writtenSongs) {
            sb.append(s).append("\n");
        }

        sb.append(", Performed songs: \n");
        for (Song s : performedSongs) {
            sb.append(s).append("\n");
        }

        return sb.toString();
    }
}
