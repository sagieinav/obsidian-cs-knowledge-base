package week4.practice.game;

import java.util.Random;

public class Util {
    public static int getRand(int minPoints, int maxPoints) {
        Random rand = new Random();
        return rand.nextInt(maxPoints) + minPoints;
    }
}
