import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'countSwaps' function below.
     *
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static void countSwaps(List<Integer> a) {
    // Write your code here
    int nswaps = 0,first,last;

    for (int i = 0; i < a.size(); i++) {

    for (int j = 0; j < a.size() - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a.get(j) > a.get(j + 1) ) {
            int temp = a.get(j);
            a.set(j,a.get(j+1));
            a.set(j + 1,temp);
            nswaps++;
        }
    }
        }

    first = a.get(0);
    last = a.get(a.size() - 1);
    System.out.println("Array is sorted in " + nswaps + " swaps.");
    System.out.println("First Element: " + first);
    System.out.println("Last Element: " + last);


    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String[] aTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> a = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aTemp[i]);
            a.add(aItem);
        }

        Result.countSwaps(a);

        bufferedReader.close();
    }
}
