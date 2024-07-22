import java.util.Arrays;
import java.util.Scanner;

public class Selecao1045 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String valores = input.nextLine();
        String[] valor = valores.split(" ");
        double[] numeros = Arrays.stream(valor).mapToDouble(Double::parseDouble).toArray();
        Arrays.sort(numeros);
        double A = numeros[2];
        double B = numeros[1];
        double C = numeros[0];

        if (A >= (B + C)) {
            System.out.println("NAO FORMA TRIANGULO");
        } else {
            if (Math.pow(A,2) == (Math.pow(B,2) + Math.pow(C,2))) {
                System.out.println("TRIANGULO RETANGULO");
            }
            if (Math.pow(A, 2) > (Math.pow(B, 2) + Math.pow(C, 2))) {
                System.out.println("TRIANGULO OBTUSANGULO");
            }
            if (Math.pow(A, 2) < (Math.pow(B, 2) + Math.pow(C, 2))) {
                System.out.println("TRIANGULO ACUTANGULO");
            }
            if (A == B && A == C) {
                System.out.println("TRIANGULO EQUILATERO");
            }
            if ((A == B && A != C) || (B == C && B != A) || (C == A && C != B)) {
                System.out.println("TRIANGULO ISOSCELES");
            }
        }
    }
}
