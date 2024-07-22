import java.util.Scanner;

public class Selecao1051 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double salario = input.nextDouble();
        double imposto = 0.0;

        if (salario <= 2000.00) {
            System.out.println("Isento");
        } else {
            if (salario > 4500.00) {
                imposto += (salario - 4500.00) * 0.28;
                salario = 4500.00;
            }
            if (salario > 3000.00) {
                imposto += (salario - 3000.00) * 0.18;
                salario = 3000.00;
            }
            if (salario > 2000.00) {
                imposto += (salario - 2000.00) * 0.08;
            }
            System.out.printf("R$ %.2f\n", imposto);
        }
    }
}
