import java.util.Scanner;

public class Sequencial1012 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        String linha = console.nextLine();
        String[] valor = linha.split(" ");
        double pi = 3.14159;
        double A = Double.parseDouble(valor[0]);
        double B = Double.parseDouble(valor[1]);
        double C = Double.parseDouble(valor[2]);

        double triangulo = (A * C) / 2;
        double circulo = pi * Math.pow(C, 2);
        double trapezio = ((A + B) * C) / 2;
        double quadrado = Math.pow(B, 2);
        double retangulo = A * B;
        System.out.printf("TRIANGULO: %.3f%n",triangulo);
        System.out.printf("CIRCULO: %.3f%n",circulo);
        System.out.printf("TRAPEZIO: %.3f%n",trapezio);
        System.out.printf("QUADRADO: %.3f%n",quadrado);
        System.out.printf("RETANGULO: %.3f%n", retangulo);

    }
}
