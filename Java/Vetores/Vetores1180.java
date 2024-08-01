import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1180 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        String x = input.readLine();
        String[] X = x.split(" ");
        int menor = Integer.MAX_VALUE;
        int posicao = 0;

        for (int i = 0; i < n; i++) {
            int N = Integer.parseInt(X[i]);

            if (N < menor) {
                menor = N;
                posicao = i;
            }
        }
        System.out.println("Menor valor: " + menor);
        System.out.println("Posicao: " + posicao);
    }
}
