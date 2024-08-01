import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1172 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] vetor = new int[10];
        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(input.readLine());
            if (n <= 0) {
                vetor[i] = 1;
            } else {
                vetor[i] = n;
            }
            System.out.println("X[" + i + "] = " + vetor[i]);
        }
    }
}
