import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1175 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] N = new int[20];

        for (int i = 0; i < N.length; i++) {
            int n = Integer.parseInt(input.readLine());
            N[i] = n;
        }

        for (int i = 0; i < N.length / 2; i++) {
            int temp = N[i];
            N[i] = N[N.length - 1 - i];
            N[N.length - 1 - i] = temp;
        }

        for (int i = 0; i < N.length; i++) {
            System.out.println("N[" + i + "] = " + N[i]);
        }
    }
}
