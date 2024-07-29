import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1117 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        double soma = 0;
        int cont = 0;
        while (cont < 2) {
            double nota = Double.parseDouble(input.readLine());
            if (nota >= 0 && nota <= 10) {
                soma += nota;
                cont++;
            } else {
                System.out.println("nota invalida");
            }
        }
        double media = soma / 2.0;
        System.out.printf("media = %.2f\n", media);
    }
}