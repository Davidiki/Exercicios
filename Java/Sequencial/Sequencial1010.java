import java.util.Scanner;

public class Sequencial1010 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        String Line1 = console.nextLine();
        String Line2 = console.nextLine();
        String[] valor1 = Line1.split(" ");
        String[] valor2 = Line2.split(" ");
        int numeroPeca1 = Integer.parseInt(valor1[1]);
        int numeroPeca2 = Integer.parseInt(valor2[1]);
        double valorUnitario1 = Double.parseDouble(valor1[2]);
        double valorUnitario2 = Double.parseDouble(valor2[2]);
        double total = (valorUnitario1 * numeroPeca1) + (valorUnitario2 * numeroPeca2);
        System.out.printf("VALOR A PAGAR: R$ %.2f%n", total);

    }
}
