import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1164 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(input.readLine());
            int soma = 0;
            for (int j = 1; j < x ; j++) {
                if (x % j == 0) {
                    soma += j;
                }
            }
            if (soma == x) {
                System.out.println(x + " eh perfeito");
            } else {
                System.out.println(x + " nao eh perfeito");
            }
        }
    }
}
