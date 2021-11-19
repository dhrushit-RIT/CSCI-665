/**
 * Cubes.java
 *
 * Version:
 * 1.0.0
 * 
 */

import java.util.Scanner;

/**
 * 
 * The program takes as input one integer - upper bound
 * it then computes and outputs the cubes of the intergers
 * such that the cube does not exceed the upper bound
 * if it does, the program stops and returns
 * 
 * Sample Input 1: 
 * 2
 * Sample Output 1:
 * 0
 * 1
 * 
 * Sample Input 2:
 * 1000
 * Sample Output 2:
 * 0
 * 1
 * 8
 * 27
 * 64
 * 125
 * 216
 * 343
 * 512
 * 729
 * 1000
 * 
 * @author Dhrushit S. Raval
 * 
 *
 */

class Cubes {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer upperBound = sc.nextInt();

        sc.close();
        Integer cube = 0;
        Integer current = 0;
        while (cube <= upperBound) {
            System.out.println(cube);
            current++;
            cube = current * current * current;
        }
    }
}