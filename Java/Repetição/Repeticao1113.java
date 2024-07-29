import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1113 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String linha = input.readLine();
            String[] valores = linha.split(" ");
            int x = Integer.parseInt(valores[0]);
            int y = Integer.parseInt(valores[1]);
            if (x == y) {
                break;
            } else if (x > y) {
                System.out.println("Decrescente");
            } else if (x < y) {
                System.out.println("Crescente");
            }
        }
    }
}
