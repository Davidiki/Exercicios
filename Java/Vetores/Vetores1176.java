import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1176 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(input.readLine());
        long[] fib = new long[61];

        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= 60; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(input.readLine());
            System.out.println("Fib(" + N + ") = " + fib[N]);
        }
    }
}
