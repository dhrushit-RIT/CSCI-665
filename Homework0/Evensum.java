
/**
 * Evensum.java
 *
 * Version:
 * 1.0.0
 * 
 */

import java.util.Scanner;

/**
 * 
 * The program takes input a numeber n, followed by n inter inputs
 * 
 * Then next n integers are processed. If it is even, it is summed up, else
 * ignored.
 * 
 * Then the sum is output on screen(sysout).
 * 
 * @author Dhrushit S. Raval
 * 
 *
 */

class Evensum {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer totalNumbers = Integer.valueOf(sc.nextLine());
        Integer evenIntegerSum = 0;

        for (int count = 0; count < totalNumbers; count++) {
            Integer currentNum = Integer.valueOf(sc.nextLine());
            if ((currentNum & 1) == 0) {
                evenIntegerSum += currentNum;
            }
        }

        System.out.println(evenIntegerSum);
        sc.close();
    }
}