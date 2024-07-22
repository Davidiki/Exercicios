import java.util.Scanner;

public class Sequencial1008 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int Number = console.nextInt();
        int horaTrabalhada = console.nextInt();
        double Salario = console.nextDouble();
        double total = horaTrabalhada * Salario;
        System.out.println("NUMBER = " + Number);
        System.out.printf("SALARY = U$ %.2f%n", total);
    }
}
