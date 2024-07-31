import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1154 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int soma = 0;
        int cont = 0;

        while (true) {
            int n = Integer.parseInt(input.readLine());

            if (n < 0) {
                break;
            } else {
                soma += n;
                cont++;
            }
        }
        double media = (double) soma / cont;
        System.out.printf("%.2f\n", media);
    }
}
