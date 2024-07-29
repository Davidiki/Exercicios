import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1101 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int m, n;
        while (true) {
            String linha = input.readLine();
            String[] valor = linha.split(" ");
            int soma = 0;
            if (Integer.parseInt(valor[0]) <= Integer.parseInt(valor[1])) {
                m = Integer.parseInt(valor[0]);
                n = Integer.parseInt(valor[1]);
            } else {
                m = Integer.parseInt(valor[1]);
                n = Integer.parseInt(valor[0]);
            }
            if (m <= 0 || n <= 0) {
                break;
            }
            for (int i = m; i <= n; i++) {
                System.out.printf("%d ", i);
                soma += i;
            }
            System.out.println("Sum=" + soma);
        }
    }
}
