import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1173 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] N = new int[10];
        int V = Integer.parseInt(input.readLine());
        N[0] = V;
        System.out.println("N[0] = " + N[0]);
        for (int i = 1; i < 10; i++) {
            N[i] = N[i - 1] * 2;
            System.out.println("N[" + i + "] = " + N[i]);
        }
    }
}
