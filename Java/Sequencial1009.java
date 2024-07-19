import java.util.Scanner;

public class Sequencial1009 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        String nome = console.nextLine();
        double salario = console.nextDouble();
        double vendas = console.nextDouble();
        double total = (vendas * 0.15) + salario;
        System.out.printf("TOTAL = R$ %.2f%n", total);
    }
}
