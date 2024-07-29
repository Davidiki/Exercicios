import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1118 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            double soma = 0;
            int notas = 0;

            while (notas < 2) {
                double nota = Double.parseDouble(input.readLine());
                if (nota >= 0 && nota <= 10) {
                    soma += nota;
                    notas++;
                } else {
                    System.out.println("nota invalida");
                }
            }

            System.out.printf("media = %.2f\n", soma / 2);

            while (true) {
                System.out.println("novo calculo (1-sim 2-nao)");
                int novoCalculo = Integer.parseInt(input.readLine());
                if (novoCalculo == 1) {
                    break;
                } else if (novoCalculo == 2) {
                    return;
                }
            }
        }
    }
}
