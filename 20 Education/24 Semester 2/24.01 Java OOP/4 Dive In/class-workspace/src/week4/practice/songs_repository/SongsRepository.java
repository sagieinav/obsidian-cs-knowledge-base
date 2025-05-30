package week4.practice.songs_repository;

public class SongsRepository {
    public enum eAddSongStatus {
        Success, SongAlreadyExists, WriterDoesNotExist, PerformerDoesNotExist
    }
    private Artist[] allArtists;
    private int numOfArtists;
    private Song[] allSongs;
    private int numOfSongs;

}

