package week4.practice.game;

public class Game {
    private static final int MAX_ROUND = 5;
    private static final int MIN_POINTS = 0;
    private static final int MAX_POINTS = 10;
    private Player player1;
    private Player player2;
    private StringBuilder result = new StringBuilder();

    public Game(String player1, String player2) {
        this.player1 = new Player(player1);
        this.player2 = new Player(player2);
    }

    public void run() {
        executeGame();
        finalResult();
    }

    public void executeGame() {
        int i1;
        int i2;
        for (int i = 1; i <= MAX_ROUND; i++){ // 5 Rounds
            i1 = Util.getRand(MIN_POINTS, MAX_POINTS);
            i2 = Util.getRand(MIN_POINTS, MAX_POINTS);
            player1.shoot(i1);
            player2.shoot(i2);
            result.append("Score gained in round ").append(i).append(":\n")
                    .append(player1.getName()).append(" has gained ").append(i1).append(" points\n")
                    .append(player2.getName()).append(" has gained ").append(i2).append(" points\n")
                    .append("\n");
        }
    }

    public void finalResult() {
        result.append("===== FINAL RESULT =====\n");
        result.append(player1.getName()).append(" has scored ").append(player1.getScore()).append(" points.\n");
        result.append(player2.getName()).append(" has scored ").append(player2.getScore()).append(" points.\n");
        if (player1.getScore() > player2.getScore()){
            result.append("This match's winner is: ").append(player1.getName());
        }
        else if (player2.getScore() > player1.getScore()) {
            result.append("This match's winner is: ").append(player2.getName());
        }
        else {
            result.append("This match has ended in a tie");
        }
        System.out.println(result);
    }
}
