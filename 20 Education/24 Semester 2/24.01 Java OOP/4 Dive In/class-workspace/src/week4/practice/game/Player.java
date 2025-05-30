package week4.practice.game;

public class Player {
    private String name;
    private int score;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }


    public Player(String name) { // Constructor #1
        this.name = name;
    }

    public void shoot (int randNum){
        this.score += randNum;
    }
}
