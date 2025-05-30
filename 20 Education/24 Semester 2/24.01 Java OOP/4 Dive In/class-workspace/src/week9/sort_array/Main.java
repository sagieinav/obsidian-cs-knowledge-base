package week9.sort_array;

import java.util.Arrays;

class Main{
    public static void main(String[] args) {
        int[] arr = {32, 5, 2, 8, 4, 6, 9, 7};
        System.out.println("Before sorting: " + Arrays.toString(arr));
        Arrays.sort(arr);
        System.out.println("After sorting: " + Arrays.toString(arr));
    }
}