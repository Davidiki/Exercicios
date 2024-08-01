import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1177 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(input.readLine());


        int[] N = new int[1000];

        for (int i = 0; i < N.length; i++) {
            N[i] = i % T;
            System.out.println("N[" + i + "] = " + N[i]);
        }
    }
}
