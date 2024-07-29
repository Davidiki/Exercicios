import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1134 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int alcool = 0, gasolina = 0, diesel = 0;
        while (true) {
            int n = Integer.parseInt(input.readLine());
            if (n == 1) {
                alcool++;
            } else if (n == 2) {
                gasolina++;
            } else if (n == 3) {
                diesel++;
            } else if (n == 4) {
                break;
            }
        }
        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Diesel: " + diesel);
    }
}
