import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1115 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String linha = input.readLine();
            String[] valor = linha.split(" ");
            int x = Integer.parseInt(valor[0]);
            int y = Integer.parseInt(valor[1]);
            if (x == 0 || y == 0) {
                break;
            } else if (x > 0 && y > 0) {
                System.out.println("primeiro");
            } else if (x < 0 && y > 0) {
                System.out.println("segundo");
            } else if (x < 0 && y < 0) {
                System.out.println("terceiro");
            } else if (x > 0 && y < 0) {
                System.out.println("quarto");
            }
        }
    }
}
