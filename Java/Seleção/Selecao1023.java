import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Selecao1023 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String linha = input.nextLine();
        String[] valor = linha.split(" ");
        double A = Double.parseDouble(valor[0]);
        double B = Double.parseDouble(valor[1]);
        double C = Double.parseDouble(valor[2]);
        double delta = Math.pow(B, 2) - 4 * A * C;
        double R1, R2;
        if (delta < 0 || A == 0) {
            System.out.println("Impossivel calcular");
        } else {
            R1 = (-B + Math.sqrt(delta)) / (2 * A);
            R2 = (-B - Math.sqrt(delta)) / (2 * A);
            System.out.printf("R1 = %.5f\n", R1);
            System.out.printf("R2 = %.5f\n", R2);

        }
    }
}
