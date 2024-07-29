import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1099 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 1; i <= n; i++) {
            int soma = 0;
            String line = input.readLine();
            String[] tokens = line.split(" ");
            int x, y;
            if (Integer.parseInt(tokens[0]) <= Integer.parseInt(tokens[1])) {
                x = Integer.parseInt(tokens[0]);
                y = Integer.parseInt(tokens[1]);
            } else {
                x = Integer.parseInt(tokens[1]);
                y = Integer.parseInt(tokens[0]);
            }
            for (int j = x + 1; j < y; j++) { // Ajuste dos limites para a soma de números ímpares entre x e y
                if (j % 2 != 0) {
                    soma += j;
                }
            }
            System.out.println(soma);
        }
    }
}