package week4.practice.songs_repository;

public class Song {
    private String name;
    private Artist writer;
    private Artist lastPerformer;

    public Song(String name, Artist writer, Artist lastPerformer) {
        this.name = name;
        this.writer = writer;
        writer.addWrittenSong(this);
        if (lastPerformer != null) {
            this.lastPerformer = lastPerformer;
            writer.addPerformedSong(this);
        }
    }

    public String getName() {
        return name;
    }

    public void setLastPerformer(Artist artist) {
        lastPerformer = artist;
    }

    @Override
    public String toString() {
        String st = name + ", " + writer.getName();
        if (lastPerformer != null) {
            st += ", " + lastPerformer.getName();
        }
        return st;
    }
}
