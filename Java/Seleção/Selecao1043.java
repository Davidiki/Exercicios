import java.util.Locale;
import java.util.Scanner;

public class Selecao1043 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        String valor = input.nextLine();
        String[] valores = valor.split(" ");
        double A = Double.parseDouble(valores[0]);
        double B = Double.parseDouble(valores[1]);
        double C = Double.parseDouble(valores[2]);
        double perimetro, area;

        if (A + B > C && B +C > A && A +C > B){
            perimetro = A + B + C;
            System.out.printf("Perimetro = %.1f\n", perimetro);
        } else{
            area = (A + B) * C / 2.0;
            System.out.printf("Area = %.1f\n", area);
        }
    }
}
