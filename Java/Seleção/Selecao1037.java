import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Selecao1037 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        double n = Double.parseDouble(input.readLine());

        if (n >= 0 && n <= 25) {
            System.out.println("Intervalo [0,25]");
        } else if (n > 25 && n <= 50) {
            System.out.println("Intervalo (25,50]");
        } else if (n > 50 && n <= 75) {
            System.out.println("Intervalo (50,75]");
        } else if (n > 75 && n <= 100) {
            System.out.println("Intervalo (75,100]");
        } else {
            System.out.println("Fora de intervalo");
        }
    }
}