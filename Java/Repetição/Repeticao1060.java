import java.util.Locale;
import java.util.Scanner;

public class Repeticao1060 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        int positivo = 0;
        for (int i = 0; i < 6; i++) {
            double n = input.nextDouble();
            if (n > 0) {
                positivo++;
            }
        }
        System.out.println(positivo + " valores positivos");
    }
}
