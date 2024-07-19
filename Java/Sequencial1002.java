import java.util.Scanner;

public class Sequencial1002 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        final double n = 3.14159;
        double raio = entrada.nextDouble();
        double area = Math.pow(raio,2) * n;
        System.out.printf("A=%.4f%n", area);
        entrada.close();
    }
}
